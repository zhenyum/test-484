import requests
import time
"""
put请求需要注意：
1.路径参数id数据库必须存在
2.修改的请求参数，goodsname在数据库唯一，不能改成和别人重复的
3.put请求是针对数据库已有的数据去修改
"""
id = 23678
url = "http://49.235.92.12:7005/api/v1/goods/{}".format(id)
body = {
    "goodsname": "《学习使用》",
    "goodscode": "sp_1646830111",
    "stock": "100",
    "price": 29
}
r = requests.put(url,json=body)
print(r.text)