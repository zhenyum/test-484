import requests
import time
goods_code = "sp_" + str(int(time.time()))
url = f"http://49.235.92.12:7005/api/v1/goods"
body = {
    "goodsname": "《学习使用》",
    "goodscode": goods_code,
}
r = requests.post(url,json=body)
print(r.text) #"id":23678
