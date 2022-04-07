import pymysql

#1.打开数据库连接,登录数据库
db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='a123456',
    db='pythonDB',)


# 2.使用cursor()方法获取操作游标
cursor = db.cursor()

#3.可以愉快的玩耍了 进行一个简单的操作
sql = 'select * from employee limit 2'
cursor.execute(sql)
rows = cursor.fetchall()
print(rows)