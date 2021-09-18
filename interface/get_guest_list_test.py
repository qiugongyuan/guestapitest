import os
import sys
import unittest
import openpyxl
import requests

from db_fixture import test_data

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

class GetGuestListTest(unittest.TestCase):
	def setUp(self):
	  self.url="http://127.0.0.1:8000/api/get_guest_list/"

	def tearDown(self):
	   print(self.result)

	def test_event_id_null(self):
		r=requests.get(self.url,params={"id":''})
		self.result=r.json()
		self.assertEqual(self.result['status'], 10021)
		self.assertEqual(self.result['message'], "id connot be empty")

	def test_event_not_exitsts(self):
		r=requests.get(self.url,params={"id":'89',"phone":'15330235989'})
		self.result=r.json()
		self.assertEqual(self.result['status'],10022)
		self.assertEqual(self.result['message'],'query result is empty')

	def test_get_event_list_success(self):
		r=requests.get(self.url,params={"id":'1','phone':'13511001100'})
		self.result=r.json()
		self.assertEqual(self.result['status'],200)
		self.assertEqual(self.result['message'],'success')

if __name__=="__main__":
	test_data.init_data()
	unittest.main()