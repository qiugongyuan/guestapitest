import unittest

import requests
from db_fixture import test_data


class AddGuestTest(unittest.TestCase):
	def setUp(self):
		self.base_url="http://127.0.0.1:8000/api/add_guest/"
	def tearDown(self):
		print(self.result)

	def test_add_guest_error(self):
		payload={'event_id':'','realname':'','phone':'','email':''}
		r=requests.post(self.base_url,data=payload)
		self.result=r.json()
		self.assertEqual(self.result['status'],10021)
		self.assertEqual(self.result["message"],'parameter error')


	def test_add_guest_test_event_null(self):
		payload = {'event_id': '39', 'realname': 'test', 'phone': '15330235989', 'email': '77899@qq.com'}
		r = requests.post(self.base_url, data=payload)
		self.result = r.json()
		self.assertEqual(self.result['status'], 10022)
		self.assertEqual(self.result["message"], 'event id null')

	def test_add_guest_test_event_status(self):
		payload = {'event_id': '3', 'realname': 'test', 'phone': '15330235989', 'email': '77899@qq.com'}
		r = requests.post(self.base_url, data=payload)
		self.result = r.json()
		self.assertEqual(self.result['status'], 10023)
		self.assertEqual(self.result["message"], 'event status is not available')

	def test_add_guest_test_event_started(self):
		payload = {'event_id': '4', 'realname': 'test', 'phone': '15330235989', 'email': '77899@qq.com'}
		r = requests.post(self.base_url, data=payload)
		self.result = r.json()
		self.assertEqual(self.result['status'], 10025)
		self.assertEqual(self.result["message"], 'event has started')

	def test_add_guest_test_event_full(self):
		payload = {'event_id': '5', 'realname': 'test', 'phone': '15330235989', 'email': '77899@qq.com'}
		r = requests.post(self.base_url, data=payload)
		self.result = r.json()
		self.assertEqual(self.result['status'], 10024)
		self.assertEqual(self.result["message"], 'event number is full')

	def test_add_guest_test_event_success(self):
		payload = {'event_id': '1', 'realname': 'test', 'phone': '15330235989', 'email': '77899@qq.com'}
		r = requests.post(self.base_url, data=payload)
		self.result = r.json()
		self.assertEqual(self.result['status'], 200)
		self.assertEqual(self.result["message"], 'add guest success')




if __name__=='__main__':
	test_data.init_data()

	unittest.main()
