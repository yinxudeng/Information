from multiprocessing import Process, Queue
import requests, json, os

url_create = "http://127.0.0.1:8000/create/"
url_update = "http://127.0.0.1:8000/update/"
header_dict = {"Content-Type": "application/json; charset=utf8"}

def info(title):
	print(title)
	print('module name:', __name__)
	print('parent process:', os.getppid())
	print('process id:', os.getpid())

def test_create():
	info('function test_create')
	person = {"name": "Sun Wu Kong", "age": 33, "city": "Shanghai", "province": "Shanghai", "phone": "1333"}
	str_person = json.dumps(person)
	response_1 = requests.post(url_create, data = str_person, headers = header_dict)
	q.put(response_1)

def test_update():
	info('function test_update')
	person = {"name": "Zhu Ba Jie", "age": 44, "city": "Beijing", "province": "Beijing", "phone": "3032093020"}
	str_person = json.dumps(person)
	response_2 = requests.post(url_update, data = str_person, headers = header_dict)
	q.put(response_2)

if __name__ == '__main__':
	response_1 = None
	response_2 = None

	q = Queue()

	info('main process')
	process_create = Process(target = test_create)
	process_update = Process(target = test_update)

	process_create.start()
	process_create.join()
	response_1 = q.get()
	if response_1.json()["message"] == "no data":
		print("Request to http://127.0.0.1:8000/create/ executed successfully")
	else:
		print("Request to http://127.0.0.1:8000/create/ failed")

	process_update.start()
	process_update.join()
	response_2 = q.get()
	if response_2.json()["message"] == "no data":
		print("Request to http://127.0.0.1:8000/update/ executed successfully")
	else:
		print("Request to http://127.0.0.1:8000/update/ failed")



