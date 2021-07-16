import unittest
import requests
from db_fixture import test_data

class GetEventListTest(unittest.TestCase):
	def setUp(self):
		self.base_url="http://127.0.0.1:8000/api/get_sec_event_list/"
	def tearDown(self):
		print(self.result)
	def test_get_event_list_auth_null(self):
		r=requests.get(self.base_url,params={'id':1})
		self.result=r.json()
		self.assertEqual(self.result['status'],10011)
		self.assertEqual(self.result['message'],'user auth null')

	def test_get_event_list_auth_fail(self):
		auth_user=('abd','test')
		r=requests.get(self.base_url,auth=auth_user,params={'id':1})
		self.result=r.json()
		self.assertEqual(self.result['status'],10012)
		self.assertEqual(self.result['message'],'user auth fail')

	def test_get_event_list_id_null(self):
		auth_user=('admin','admin123456')
		r=requests.get(self.base_url,auth=auth_user,params={'id':''})
		self.result=r.json()
		self.assertEqual(self.result['status'],10021)
		self.assertEqual(self.result['message'],'parameter error')
	def test_get_event_list_success(self):
		auth_user=('admin','admin123456')
		r=requests.get(self.base_url,auth=auth_user,params={'id':'1'})
		self.result=r.json()
		self.assertEqual(self.result['status'],200)
		self.assertEqual(self.result['message'],'success')

if __name__=='__main__':
	test_data.init_data()
	unittest.main()