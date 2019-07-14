from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from information.crud.models import Person
from django.core.exceptions import ValidationError
import json, logging

stdlogger = logging.getLogger('views')
dbalogger = logging.getLogger('dba')

def check_post_request(function):
	def wrapper(request):
		if request.method == 'POST':
			try:
				result = json.loads(request.body)
			except:
				stdlogger.error("POST request's body was empty")
				return HttpResponseNotAllowed(["POST request's body was empty"])
			if result:
				return function(request)
			else:
				stdlogger.error("POST request was not empty but had no contents inside {}")
				return HttpResponseNotAllowed(["POST request was not empty but had no contents inside brackets {}"])
		else:
			stdlogger.error("Request was not POST")
			return HttpResponseNotAllowed(["Request was not POST"])
	return wrapper

# Create your views here.
@csrf_exempt
@check_post_request
def create(request):
	stdlogger.info("Entering CREATE method")
	result = json.loads(request.body)
	try:
		person = Person(name = result['name'], age = result['age'], city = result['city'], province = result['province'], phone = result['phone'])
		person.validate_unique()
		person.clean_fields()
	except KeyError:
		dbalogger.error("Entry does not have enough values")
		return JsonResponse({"message": "Entry does not have enough values", "data": None})
	except ValidationError:
		dbalogger.error("Entry's values do not fulfill requirements")
		return JsonResponse({"message": "Entry's values do not fulfill requirements", "data": None})
	person.save()
	dbalogger.info("Entry was created successfully")
	stdlogger.info("CREATE method executed successfully")
	return JsonResponse({"message": "no data", "data": None})

@csrf_exempt
@check_post_request
def read(request):
	stdlogger.info("Entering READ method")
	result = json.loads(request.body)
	try:
		person = Person.objects.get(phone = result['phone'])
	except:
		dbalogger.error("Requested entry does not exist in database")
		return JsonResponse({"message": "Requested entry does not exist in database", "data": None})
	dictionary = {"name": person.name, "age": person.age, "city": person.city, "province": person.province, "phone": person.phone}
	dbalogger.info("Entry was read successfully")
	stdlogger.info("READ method executed successfully")
	return JsonResponse(dictionary)

@csrf_exempt
@check_post_request
def update(request):
	stdlogger.info("Entering UPDATE method")
	result = json.loads(request.body)
	try:
		person = Person.objects.get(phone = result['phone'])
	except:
		dbalogger.error("Requested entry does not exist in database")
		return JsonResponse({"message": "Requested entry does not exist in database", "data": None})
	try:
		person.name = result['name']
		person.age = result['age']
		person.city = result['city']
		person.province = result['province']
		person.clean_fields()
	except KeyError:
		dbalogger.error("Entry does not have enough values")
		return JsonResponse({"message": "Entry does not have enough values", "data": None})
	except ValidationError:
		dbalogger.error("Entry's values do not fulfill requirements")
		return JsonResponse({"message": "Entry's values do not fulfill requirements", "data": None})
	person.save()
	dbalogger.info("Entry was updated successfully")
	stdlogger.info("UPDATE method executed successfully")
	return JsonResponse({"message": "no data", "data": None})

@csrf_exempt
@check_post_request
def delete(request):
	stdlogger.info("Entering DELETE method")
	result = json.loads(request.body)
	try:
		person = Person.objects.get(phone = result['phone'])
	except:
		dbalogger.error("Requested entry does not exist in database")
		return JsonResponse({"message": "Requested entry does not exist in database", "data": None})
	person.delete()
	dbalogger.info("Entry was deleted successfully")
	stdlogger.info("DELETE method executed successfully")
	return JsonResponse({"message": "no data", "data": None})

