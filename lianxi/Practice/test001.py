import MySQLdb
# 连接mysql数据库，不加charset="utf8"，打印的中文是乱码
connction=MySQLdb.Connect(
                    host='127.0.0.1',
                    user='root',
                    password='liwx011518',
                    database='practice',
                    port=3306,
                    charset="utf8")
# 通过cursor创建游标
cursor=connction.cursor()

# SQL语句查询student表中所有记录
sql_1="select * from  students"

sql_2="select t.tname as 教师姓名, t.tsex as 性别, t.depart as 课程 from teachers t"

# 执行sql语句
cursor.execute(sql_1)

# 获取一条数据，返回的是一个元祖，里面每一个元素代表一个字段
result1=cursor.fetchone()

print(result1)
cursor.execute(sql_2)
result1=cursor.fetchone()

print(result1)


