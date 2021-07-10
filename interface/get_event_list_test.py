import requests
import unittest

class GetEventListTest(unittest.TestCase):
    def setUp(self):
            self.url="http://127.0.0.1:8000/api/get_event_list/"


    def test_get_event_null(self):
        r=requests.get(self.url,params={"id":''})
        result=r.json()
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],"parameter error")

if __name__=='__main__':
    if __name__ == '__main__':
        unittest.main()
