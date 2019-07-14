import requests, json, threading

url_create = "http://127.0.0.1:8000/create/"
url_update = "http://127.0.0.1:8000/update/"
header_dict = {"Content-Type": "application/json; charset=utf8"}

class myThread(threading.Thread):
	def __init__(self, threadID, name, url):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.url = url
	def run(self):
		if self.url == url_create:
			test_create()
		elif self.url == url_update:
			test_update()

def test_create():
	global response_1
	person = {"name": "Lao Li Tou", "age": 148, "city": "Wuhan", "province": "Hubei", "phone": "023232323"}
	str_person = json.dumps(person)
	response_1 = requests.post(url_create, data=str_person, headers = header_dict)

def test_update():
	global response_2
	person = {"name": "Lao Wang Tou", "age": 55, "city": "Wuhan", "province": "Hubei", "phone": "303209300"}
	str_person = json.dumps(person)
	response_2 = requests.post(url_update, data=str_person, headers = header_dict)

thread1 = myThread(1, "Thread-1-create", url_create)
thread2 = myThread(2, "Thread-2-update", url_update)

response_1 = None
response_2 = None

thread1.start()
thread1.join()
if response_1.json()["message"] == "no data":
	print("Request to http://127.0.0.1:8000/create/ executed successfully")
else:
	print("Request to http://127.0.0.1:8000/create/ failed")

thread2.start()
thread2.join()
if response_2.json()["message"] == "no data":
	print("Request to http://127.0.0.1:8000/update/ executed successfully")
else:
	print("Request to http://127.0.0.1:8000/update/ failed")