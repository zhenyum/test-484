import pytest,allure,os
allure.title("登录接口")
# 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录,生成临时的json文件路径
pytest.main(['--alluredir', './temp'])
#  执行命令 allure generate ./temp -o ./report --clean ，生成测试报告

