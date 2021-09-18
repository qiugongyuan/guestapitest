import hashlib
import json
import unittest
from time import time

import requests


class AddEventTest(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/add_sec_event/"
        # app_key
        self.api_key = "&Guest-Bugmaster"

        # 当前时间
        now_time = time()
        print(now_time)
        self.client_time = str(now_time).split('.')[0]
        print(self.client_time)
        # sign
        md5 = hashlib.md5()
        sign_str = self.client_time + self.api_key
        sign_bytes_utf8 = sign_str.encode(encoding='utf-8')
        md5.update(sign_bytes_utf8)
        self.sign_md5 = md5.hexdigest()

    def tearDown(self):
        print(self.result)

    def test_add_sec_event_error(self):
        r = requests.get(self.base_url)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10011)
        self.assertEqual(self.result['message'], 'request error')

    def test_add_sec_event_sign_null(self):
        payload = {"id": "61", "name": "61", "limit": "2", "address": "jiayu", "start_time": "2021-07-09 12:00:00", ' \
                  '"sign": ""}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10012)
        self.assertEqual(self.result['message'], 'user sign null')

    # def test_add_event_time_out(self):
    #     now_time=str(int(self.client_time)-61)
    #     payload = {"id": "63", "name": "63", "limit": "2", "address": "jiayu", "start_time": "2021-07-09 12:00:00",
    #                      "sign":self.sign_md5,'time':now_time}
    #     r=requests.post(self.base_url,data=payload)
    #     self.result=r.json()
    #     self.assertEqual(self.result['status'],10013)
    #     self.assertEqual(self.result['message'],'user sign timeout')

    def test_add_sec_event_sign_error(self):
        payload = {"id": "62", "name": "62", "limit": "2", "address": "jiayu", "start_time": "2021-07-09 12:00:00",
                   "sign": 'hello', 'time': self.client_time}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10014)
        self.assertEqual(self.result['message'], 'user sign error')

    def test_add_sec_event_success(self):
        payload = {"id": "61", "name": "61", "limit": "2", "address": "jiayu", "start_time": "2021-07-09 12:00:00",
                   "sign": self.sign_md5, 'time': self.client_time}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add event success')


if __name__ == '__main__':
    unittest.main()
