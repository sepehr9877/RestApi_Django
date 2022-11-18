import json
import unittest
import requests
class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account_url="http://127.0.0.1:8000/AccountApi"
        self.headers={}
        self.headers['content-type']="application/json"
    def test_getmethod_getalluser(self):
        method="get"
        data=requests.request(method=method,url=self.account_url,headers=self.headers)
        json_data=json.loads(data.text)
        print(json_data)
