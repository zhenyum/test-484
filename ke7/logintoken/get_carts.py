from ke7.login_function import login
import requests
token = login(user='test15')
print(token)
headers = {
    "Authorization": "Token {}".format(token)
}
url = "http://49.235.92.12:7005/api/v2/carts"
r = requests.get(url,headers=headers)
print(r.text)

# #添加商品到购物车
body = {
    "goodscode": "sp_1646880641",
    "goodsnum": 10
}
r2 = requests.post(url,headers=headers,json=body)
print(r2.text)