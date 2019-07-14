from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from information.crud.models import Person
import ast, xlrd, logging

stdlogger = logging.getLogger('views')
dbalogger = logging.getLogger('dba')

# Create your views here.
@csrf_exempt
def upload(request):
	if request.method == 'POST':
		stdlogger.info("Entering UPLOAD method")
		try:
			media = request.FILES.get('media', None)
		except:
			stdlogger.info("No file was uploaded")
			return JsonResponse({"message": "No file was uploaded", "data": None})
		if not media:
			stdlogger.info("No file was uploaded")
			return JsonResponse({"message": "No file was uploaded", "data": None})
		media_name = '%s/%s' % (settings.MEDIA_PATH, media.name)
		name_list = media_name.split(".")
		with open(media_name, 'wb') as f:
			for fmedia in media.chunks():
				f.write(fmedia)
		stdlogger.info("File was uploaded successfully")
		person_list = []
		if name_list[-1] == "xlsx":
			data = xlrd.open_workbook(media_name)
			table = data.sheet_by_name("Sheet1")
			for i in range(table.nrows):
				row_data = table.row_values(i)
				new_person = Person(name = row_data[0], age = int(row_data[1]), city = row_data[2], province = row_data[3], phone = str(int(row_data[4])))
				person_list = person_list + [new_person]
			Person.objects.bulk_create(person_list)
			dbalogger.info("Entires were transferred from an Excel file to database successfully")
			stdlogger.info("UPLOAD method executed successfully")
			return JsonResponse({"message": "Excel file was uploaded successfully, and data was imported into database successfully", "data": None})
		else:
			with open(media_name, 'r') as f:
				contents = f.readlines()
			for dictionary_string in contents:
				dictionary = ast.literal_eval(dictionary_string)
				new_person = Person(name = dictionary["name"], age = dictionary["age"], city = dictionary["city"], province = dictionary["province"], phone = dictionary["phone"])
				person_list = person_list + [new_person]
			Person.objects.bulk_create(person_list)
			dbalogger.info("Entries were transferred from a text file to database successfully")
			stdlogger.info("UPLOAD method executed successfully")
			return HttpResponse("Text file was uploaded successfully, and data was imported into database successfully")
	else:
		stdlogger.error("Request was not POST")
		return HttpResponseNotAllowed(["Request was not POST"])