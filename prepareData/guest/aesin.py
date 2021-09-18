import json
from Crypto.Cipher import AES
import base64

from django.contrib.sites import requests

app_key = 'W7v4D60fds2Cmk2U'
base_url = 'http://127.0.0.1:8000/api/aes_get_guest_list/'


class cryptAES(object):
    def __init__(self):
        self.BS = 16
        self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)

    def encryptBase64(self, src):
        base64_message = base64.urlsafe_b64encode(src)
        return base64_message

    def encryptAES(self, src, key):
        iv = b'1172311105789011'
        cryptor = AES.new(key.encode(), AES.MODE_CBC, iv)
        ciphertext = cryptor.encrypt(self.pad(src).encode('utf-8'))
        base64_msg = self.encryptBase64(ciphertext)
        return base64_msg


if __name__ == "__main__":
    payload = {'id': '1', 'phone': '18511853177'}
    myCryptor = cryptAES()
    encoded = myCryptor.encryptAES(json.dumps(payload), app_key).decode()
    print(encoded)




