import requests
url1 = "http://49.235.92.12:7005/api/v1/login"
body = {
    "username": "test1",
    "password": "123456"
}
r = requests.post(url1,json=body)
print(r.text) #登录成功

#获取token
token = r.json().get('token')
print('获取到的token:',token)
headers = {
    "Authorization": "Token {}".format(token)
}
sp_id = 1
url2 = "http://49.235.92.12:7005/api/v2/goods/{}".format(sp_id)
r2 = requests.get(url2,headers=headers)
print(r2.text)