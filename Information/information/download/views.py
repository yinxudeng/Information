from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from information.crud.models import Person
from django.utils.encoding import escape_uri_path
import xlsxwriter, logging

stdlogger = logging.getLogger('views')
dbalogger = logging.getLogger('dba')

# Create your views here.
@csrf_exempt
def export_excel(request):
	if request.method == 'GET':
		stdlogger.info("Entering EXPORT_EXCEL method")
		try:
			city = request.GET.get('city')
			province = request.GET.get('province')
		except:
			stdlogger.error("GET request does not have enough values")
			return JsonResponse({"message": "GET request does not have enough values", "data": None})
		file_name = province + '_' + city + '.xlsx'
		age_between_20_and_50 = Person.objects.filter(city = city, province = province, age__gte = 20, age__lte = 50)
		if age_between_20_and_50:
			media_name = '%s/%s' % (settings.DOWNLOAD_PATH, file_name)
			workbook = xlsxwriter.Workbook(media_name)
			worksheet1 = workbook.add_worksheet('Sheet1')
			excel_row = 0
			for person in age_between_20_and_50:
				worksheet1.write(excel_row, 0, person.name)
				worksheet1.write(excel_row, 1, person.age)
				worksheet1.write(excel_row, 2, person.city)
				worksheet1.write(excel_row, 3, person.province)
				worksheet1.write(excel_row, 4, person.phone)
				excel_row += 1
			workbook.close()
			dbalogger.info("Entries were transferred to a local Excel file successfully")
			with open(media_name, 'rb') as model_excel:
				result = model_excel.read()
			response = HttpResponse(result)
			response['Content-Type'] = 'application/octet-stream'
			response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path(file_name))
			stdlogger.info("Excel file was downloaded successfully")
			stdlogger.info("EXPORT_EXCEL method executed successfully")
			return response
		else:
			dbalogger.error("Request entry does not exist in database")
			return JsonResponse({"message": "Requested entry does not exist in database", "data": None})
	else:
		stdlogger.error("Request was not GET")
		return HttpResponseNotAllowed(["Request was not GET"])