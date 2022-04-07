import pytest
import jsonpath
from test_youyou.common.utils import *
datas = read_yaml(data_path+'/login.yaml')#读取yaml中的测试数据
@pytest.mark.parametrize('url,method,data,assert_msg',datas)
def test_login(url,method,data,assert_msg):
    r = request(url,method,json=data)
    print(r.json())
    msg = ''.join(jsonpath.jsonpath(r.json(), '$.msg'))
    assert msg == assert_msg
# if __name__ == '__main__':#一般不在用例下执行 写到run里面
#     pytest.main(['-v',__file__])