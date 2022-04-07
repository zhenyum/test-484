            项目简介 接口自动化项目，环境-python 3
基于pytest+yaml+allure,接口关联的封装，一般情况下，
我们是通过一个关联的yaml文件来实现的

项目架构：
case：用于保存每个接口的测试脚本
    demo_case------>演示demo用例
    xxx_case------->各业务测试用例
common：保存公共模块，比如数据库操作类、yaml文件读取，邮件基础
    utils-常用方法
api: 各种需要用到的接口
    commom_api----->公共api
    xxx_api------>各业务api
data：保存每个接口的测试用例（yaml文件）
    extract.yml:存放接口关联的数据

report：用于保存测试报告

run:程序主入口