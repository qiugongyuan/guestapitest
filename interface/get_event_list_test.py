import os,sys
import requests
import unittest
sys.path.append('../db_fixture')
from db_fixture import test_data

class GetEventListTest(unittest.TestCase):
    def setUp(self):
        self.url="http://127.0.0.1:8000/api/get_event_list/"


    def test_get_event_null(self):
        r=requests.get(self.url, params={"id":''})
        result=r.json()
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],"parameter error")

    def test_get_event_error(self):
        r=requests.get(self.url, params={"id":"90"})
        result=r.json()
        self.assertEqual(result['status'],10022)
        self.assertEqual(result['message'],"query result is empty")

    def test_get_event_success(self):
        r=requests.get(self.url, params={"id":"2"})
        result=r.json()
        print(result)
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],"success")
        self.assertEqual(result['data']['name'],"可参加人数为0")
        self.assertEqual(result['data']['address'],'北京会展中心')


if __name__ == '__main__':

    test_data.init_data()   # 初始化接口测试数据

    unittest.main()
