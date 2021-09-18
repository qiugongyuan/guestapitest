
import re

import requests

base_url = "http://127.0.0.1:8000"
i = 0
a = 0
with open('C:\\Users\\zhaoj\\Desktop\\sign_guest_new.csv', 'r', encoding="utf-8") as testfile:
    for phone in testfile:
        phone = re.sub(r"[^0-9]", "", phone)
        datas = {'id': 1, 'phone': phone}
        print(datas)
        r = requests.post(base_url + '/api/user_sign/', data=datas)
        result = r.json()
        print(result)
        try:
            assert result['message'] == "sign success"
            i = i + 1
        except AssertionError as e:
            print("phone:" + str(phone) + ",user sign fail!" + str(e))
            a = a + 1
print(i)
print(a)
