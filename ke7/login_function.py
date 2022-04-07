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
    print(r.text)

    # 获取token
    token = r.json().get('token')
    print('获取到的token:', token)
    return token
#封装一个md5的加密函数
def get_md5(psw='123456'):
    #实例化一个md5对象
    md5 = hashlib.md5()
    #调用加密方法加密
    md5.update(psw.encode("utf-8"))
    return md5.hexdigest()
if __name__ == "__main__":
    t = login()
    print(get_md5())