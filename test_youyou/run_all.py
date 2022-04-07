import pytest,os
from test_youyou.common.utils import case_path,report_path,get_time
t = get_time()#获取当前时间
pytest.main(['--alluredir', './report/temp'])
os.system('allure generate ./report/temp -o ./report/html --clear')