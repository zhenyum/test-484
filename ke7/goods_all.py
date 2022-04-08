import requests
url = "http://49.235.92.12:7005/api/v1/goods"
params = {
    "page":5,#有bug 没生效
    "size":3
}
r = requests.get(url,params=params)
#print(r.text)
print(r.json())