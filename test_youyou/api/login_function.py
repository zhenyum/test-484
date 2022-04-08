import requests
import hashlib
def login(user="test1",psw="123456"):
    """
    登录函数
    """
    url1 = "http://49.235.92.12:7005/api/v1/login"
    body = {
        "username": user,
        "password": psw
    }
    r = requests.post(url1, json=body)
    # 获取token
    token = r.json().get('token')
    print('获取到的token:', token)

