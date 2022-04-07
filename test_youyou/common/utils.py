import time, os, yaml,pytest,json
import requests

base_path = os.path.dirname(os.path.dirname(__file__))# 项目基本路径
case_path = os.path.join(base_path, "case")# 测试脚本所在目录
data_path = os.path.join(base_path, "data")# 测试用例所在目录
report_path = os.path.join(base_path,"report")# 测试报告所在目录
print(base_path,case_path,data_path,report_path)
def request(url,method,data=None,json=None,header=None,**kwargs):
    rq = requests.session()  #创建session对象
    if method in ('get','GET','Get'):
        r = rq.get(url=url,params=data,headers=header,**kwargs)
    elif method in ('post','POST','Post'):
        r = rq.post(url=url,json=json,headers=header,**kwargs)
    return r
def get_time():
    t = time.strftime("%Y-%m-%d, %H:%M:%S")
    return t

def read_yaml(file):
    if os.path.exists(file):
        with open(file=file,mode='r',encoding='utf-8') as f:
            file_content = yaml.safe_load(f)
        datas = [tuple(i.values())[1::] for i in file_content]
        return datas
    else:
        print(f'文件 {file} 不存在')
        return False

def write_yaml(file,data):
    if os.path.exists(file):
        with open(file=file, mode='w',encoding='utf-8') as f:
          yaml.dump(data=data,stream=f,allow_unicode=True)
    else:
        print(f'文件 {file} 不存在')
        return False

if __name__ == '__main__':
    pytest.main()
    # data = read_yaml(data_path + '/login.yaml')
    # print(data)
