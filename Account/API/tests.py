import os.path


from django.test import TestCase
import json
import unittest
import requests
from requests.auth import HTTPBasicAuth
class TestAccount(unittest.TestCase):

    def setUp(self):
        self.detail_url="http://127.0.0.1:8000/GetAccountDetail/"
        self.register_url="http://127.0.0.1:8000/Register/"
        self.login_url="http://127.0.0.1:8000/LoginPage/"
        self.update_get_url="http://127.0.0.1:8000/UpdateUser/"
        self.headers={}
        self.user_id=None
        self.headers['content-type']="application/json"
    def test_login(self):
        method="post"
        data={"username":"sepehr",
              "password":"sepehr12345"}
        response=requests.request(method=method,url=self.login_url,data=json.dumps(data),headers=self.headers)
        print(response.text)
    def test_get_all_detail(self):
        method="get"
        print("userd")
        data={"id":"1"}
        response=requests.request(method=method,url=self.detail_url,data=json.dumps(data),headers=self.headers)
        respond_data=json.loads(response.text)
        for item in respond_data:
            for key in item:
                print(item[key])
    def test_create_user(self):
        method="post"
        with open('../images/user.jpg', 'rb') as imagefile:
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
