from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from information.crud.models import Person
import json, logging

stdlogger = logging.getLogger('views')
dbalogger = logging.getLogger('dba')

# Create your views here.
@method_decorator(csrf_exempt, name = 'dispatch')
class Query(View):
	def get(self, request):
		stdlogger.error("Request was not POST")
		return HttpResponseNotAllowed(["Request was not POST"])
	def post(self, request):
		stdlogger.info("Entering QUERY method")
		try:
			result = json.loads(request.body)
		except:
			stdlogger.error("POST request's body was empty")
			return JsonResponse({"message": "POST request's body was empty", "data": None})
		if result:
			try:
				age_between_20_and_50 = Person.objects.filter(city = result['city'], province = result['province'], age__gte=20, age__lte=50)
				dictionary = {}
			except:
				dbalogger.error("Entry does not have enough values")
				return JsonResponse({"message": "Entry does not have enough values", "data": None})
			if not age_between_20_and_50:
				dbalogger.error("Requested entry does not exist in database")
				return JsonResponse({"message": "Requested entry does not exist in database", "data": None})
			for person in age_between_20_and_50:
				individual_dictionary = {"name": person.name, "age": person.age, "city": person.city, "province": person.province, "phone": person.phone}
				dictionary[person.phone] = individual_dictionary
			stdlogger.info("QUERY method executed successfully")
			return JsonResponse(dictionary)
		else:
			stdlogger.error("POST request was not empty but had no contents inside brackets {}")
			return HttpResponseNotAllowed(["POST request was not empty but had no contents inside brackets {}"])