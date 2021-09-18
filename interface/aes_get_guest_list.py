import json
import unittest
# ! python3
# from pycryptodome import AES
from Crypto.Cipher import AES
from myConstDef import *
import requests
import base64


class AESTest(unittest.TestCase):
    def setUp(self):
        BS = 16
        self.pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        self.base_url = 'http://127.0.0.1:8000/api/aes_get_guest_list/'
        self.app_key = 'W7v4D60fds2Cmk2U'
        printInfo(self.base_url)
        printInfo(self.app_key)

    def encryptBase64(self, src):
        base64_message = base64.urlsafe_b64encode(src)
        printInfo(base64_message)
        return base64_message

    def encryptAES(self, src, key):
        iv = b'1172311105789011'
        cryptor = AES.new(key.encode(), AES.MODE_CBC, iv)
        # printInfo('''before encrypt:{}'''.format(src))
        # print(key)
        ciphertext = cryptor.encrypt(self.pad(src).encode('utf-8'))
        # printInfo('''after encrypt:{}'''.format(ciphertext))
        base64_msg = self.encryptBase64(ciphertext)
        # printInfo('''after encrypt_base64:{}'''.format(base64_msg))
        return base64_msg

    def test_aes_interface(self):
        payload = {'id': '1', 'phone': '18511853177'}
        encoded = self.encryptAES(json.dumps(payload), self.app_key).decode()
        r = requests.get(self.base_url, params={"data": encoded})
        r.content.decode("utf-8")
        result = r.json()
        # printInfo('''status:{},message:{}'''.format(result['status'], result['message']))
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'success')


if __name__ == '__main__':
    unittest.main()
