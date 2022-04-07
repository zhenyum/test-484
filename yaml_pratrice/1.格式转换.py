import yaml
#打开yaml文件
def read_yaml(filename):
    files = open(filename, 'r', encoding='utf-8')#../data/login.yaml
    #通过yaml加载文件 dict of list 称之为字典列表
    data = yaml.safe_load(files)
    return data
if __name__ == '__main__':
    file1 = read_yaml('/login.yaml')
    print(file1)