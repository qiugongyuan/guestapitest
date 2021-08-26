import unittest

import requests
from db_fixture import test_data


class UerSignTest(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/user_sign/"

    def tearDown(self):
        print(self.result)

    def test_user_sign_error(self):
        payload = {"id": '', "phone": ""}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_user_sign_event_id_null(self):
        payload = {'id': '555', 'phone': '13511001100'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event id null')

    def test_user_sign_event_phone_null(self):
        payload = {'id': '1', 'phone': '18511852669'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10025)
        self.assertEqual(self.result['message'], 'user phone null')

    def test_user_sign_event_started(self):
        payload = {'id': '4', 'phone': '13511001100'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertEqual(self.result['message'], 'event has started')

    def test_user_sign_sign_already(self):
        payload = {'id': '1', 'phone': '13511001100'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10027)
        self.assertEqual(self.result['message'], 'user has sign in')

    def test_user_sign_not_participate(self):
        payload = {'id': '1', 'phone': '15444454555'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10026)
        self.assertEqual(self.result['message'], 'user did not pacticipate in the conference')

    def test_user_sign_sign_success(self):
        payload = {'id': '1', 'phone': '15330235989'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'sign success')


if __name__ == '__main__':
    test_data.init_data()
    unittest.main()
