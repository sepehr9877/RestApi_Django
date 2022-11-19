import os.path

from django.test import TestCase
import json
import unittest
import requests
class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account_url="http://127.0.0.1:8000/AccountApi"
        self.register_url="http://127.0.0.1:8000/Register/"
        self.headers={}
        self.headers['content-type']="application/json"
    def test_getmethod_getalluser(self):
        method="get"
        data=requests.request(method=method,url=self.account_url,headers=self.headers)
        json_data=json.loads(data.text)
        print(json_data)
    def test_create_user(self):
        method="post"
        with open('images/user.jpg','rb') as imagefile:
            data={
                "country": "USA",
                "username": "Harry",
                "firstname": "Harry",
                "password": "Harry12345",
                "repassword": "Harry12345",
                "phone":None,
                "email": "harry@yahoo.com"
            }
            file={'image':imagefile}
            response=requests.request(method=method,url=self.register_url,data=data,files=file,headers={})
            print(response.text)

# Create your tests here.
