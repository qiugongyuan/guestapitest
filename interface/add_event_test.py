import os.path
import sys
import unittest
import requests

from db_fixture import test_data
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import os


class AddEventTest(unittest.TestCase):
	def setUp(self):
		self.base_url="http://127.0.0.1:8000/api/add_event/"
	def tearDown(self):
	    print(self.result)

	def test_add_event_all_null(self):
		payload={'id':'','name':'','limit':'','address':'','start_time':''}
		r=requests.post(self.base_url,data=payload)
		self.result=r.json()
		self.assertEqual(self.result['status'],10021)
		self.assertEqual(self.result['message'],'parameter error')

	def test_add_event_id_alreadyexists(self):
		payload={'id':'1','name':'test1','limit':'2','address':'jiayu','start_time':'2021-07-14 12:00:00'}
		r=requests.post(self.base_url,data=payload)
		self.result=r.json()
		self.assertEqual(self.result['status'],10022)
		self.assertEqual(self.result['message'],'event id already exists')

	def test_add_event_name_alreadyexists(self):
		payload={'id':'20','name':'红米Pro发布会','limit':'2','address':'jiayu','start_time':'2021-07-14 12:00:00'}
		r=requests.post(self.base_url,data=payload)
		self.result=r.json()
		self.assertEqual(self.result['status'], 10023)
		self.assertEqual(self.result['message'],'event name already exists')

	def test_add_event_timeformat(self):
		payload={'id':'11','name':'添加发布会18','limit':'2','address':'jiayu','start_time':'2021-07'}
		r=requests.post(self.base_url,data=payload)
		self.result=r.json()
		self.assertEqual(self.result['status'], 10024)
		self.assertEqual(self.result['message'],'start_time format error.It must be in YYYY-MM-DD HH:MM:SS format.')

	def test_add_event_success(self):
		payload={'id':'55', 'name':'添加发布会55','limit':'2','address':'jiayu','start_time':'2021-07-09 12:00:00'}
		r=requests.post(self.base_url,data=payload)
		self.result=r.json()
		self.assertEqual(self.result['status'],200)
		self.assertEqual(self.result['message'],'add event success')







if __name__=='__main__':

	test_data.init_data()
	unittest.main()