import json

import requests

def EndPointCheck(url):
    request=requests.get(url)
    mydata=json.loads(request.text)
    for item in mydata:
        print(item)
def updata_endpoint(url,data):
    headers={}
    headers['content-type']='application/json'
    passing_data=json.dumps(data)
    method="get"
    print(passing_data)
    myrequest=requests.request(url=url,method=method,headers=headers,data=passing_data)
    print(myrequest.text)



url="http://127.0.0.1:8000/Products/"
detailurl="http://127.0.0.1:8000/Products/?id=1"
# EndPointCheck(detailurl)
updata_endpoint(url,data={"id":'1'})