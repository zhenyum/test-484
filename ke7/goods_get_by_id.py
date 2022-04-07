import requests
id = 23680
url = "http://49.235.92.12:7005/api/v1/goods/{}".format(id)
r = requests.get(url)
print(r.text)