import requests
import time
print(int(time.time()))
#生成带时间戳的username
user = "test_" + str(int(time.time()))
print('每次生成不一眼的账号:',user)
url = f"http://49.235.92.12:7005/api/v1/register"
body = {
    "username": user,
    "password": "123456"
}
r = requests.post(url,json=body)
print(r.json())
