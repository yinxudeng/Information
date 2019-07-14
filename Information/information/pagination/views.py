from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from information.crud.models import Person
import json, logging

stdlogger = logging.getLogger('views')

# Create your views here.
@csrf_exempt
def show_page(request):
	if request.method == 'POST':
		stdlogger.error("Request was not GET")
		return HttpResponseNotAllowed(["Request was not GET"])
	else:
		stdlogger.info("Entering SHOW_PAGE method")
		try:
			page = request.GET.get('page')
			size = int(request.GET.get('size'))
		except:
			stdlogger.error("GET request does not have enough values")
			return JsonResponse({"message": "GET request does not have enough values", "data": None})
		result = {}
		people_list = Person.objects.all()
		paginator = Paginator(people_list, size)
		result['total'] = paginator.count
		try:
			people = paginator.page(page)
		except PageNotAnInteger:
			stdlogger.error("Page number was not an integer")
			people = paginator.page(1)
		except EmptyPage:
			stdlogger.error("Page number was out of range")
			people = paginator.page(paginator.num_pages)
		result['list'] = json.loads(serializers.serialize("json", people))
		stdlogger.info("SHOW_PAGE method executed successfully")
		return JsonResponse(result)