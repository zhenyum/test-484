import yaml,os,requests,pytest
base_path = os.path.dirname( os.path.dirname(__file__))
yaml_path = os.path.join(base_path,'yaml_pratrice')
print(yaml_path)
def read_yaml(file):
    if os.path.exists(file):
        with open(file=file,mode='r',encoding='utf-8') as f:
            file_content = yaml.safe_load(f)
        datas = [tuple(i.values())[1::] for i in file_content]
        print(file_content)
        return datas
    else:
        print(f'文件 {file} 不存在')
        return False

def write_yaml(file,data):
    if os.path.exists(file):
        with open(file=file, mode='a',encoding='utf-8') as f:
          yaml.dump(data=data,stream=f,allow_unicode=True)
    else:
        print(f'文件 {file} 不存在')
        return False
def clear_yaml(file):
    if os.path.exists(file):
        with open(file=file, mode='a',encoding='utf-8') as f:
          f.truncate()
    else:
        print(f'文件 {file} 不存在')
        return False

def request(url,method,data=None,json=None,header=None,**kwargs):
    rq = requests.session()  #创建session对象
    if method in ('get','GET','Get'):
        r = rq.get(url=url,params=data,headers=header,**kwargs)
    elif method in ('post','POST','Post'):
        r = rq.post(url=url,json=json,headers=header,**kwargs)
    return r
if __name__ == '__main__':
    pytest.main(['-v',__file__])
#     data = write_yaml(yaml_path + '/acces.yaml',{"status": 1})
#     print(data)
