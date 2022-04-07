from yaml_pratrice.yaml_util import *
import pytest
datas = read_yaml('/Python_test/yaml_pratrice/test.yaml')
@pytest.mark.parametrize('url,method,data,validate',datas)
def test_login_success(url,method,data,validate):
    r = request(url,method,json=data)
    print(r.text)
if __name__ == '__main__':
    pytest.main(['-s',__file__])
