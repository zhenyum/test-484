from yaml_pratrice.yaml_util import *
import jsonpath
import pytest
datas = read_yaml(yaml_path + '/test.yaml')
@pytest.mark.parametrize('url,method,data,assert_msg',datas)
def test_login_success(url,method,data,assert_msg):
    r = request(url,method,json=data)
    s = r.json()
    token = s.get('token')
    print('获取到的token:', token)
    write_yaml(yaml_path + '/acces.yaml',{"access_token": token})
    #msg = jsonpath.jsonpath(s, '$.msg')  # ['login success!']获取的是列表
    msg = ''.join(jsonpath.jsonpath(s, '$.msg'))#将列表转为字符串
    assert msg == assert_msg

