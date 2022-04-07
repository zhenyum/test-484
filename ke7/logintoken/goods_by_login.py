from ke7.login_function import login
import requests

token = login() #调用函数获取token
headers = {
    "Authorization": "Token {}".format(token)
}
sp_id = 1
url2 = "http://49.235.92.12:7005/api/v2/goods/{}".format(sp_id)
r2 = requests.get(url2,headers=headers)
print(r2.text)