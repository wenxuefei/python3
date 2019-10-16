import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='python_ed', port=3306)

# 创建游标对象
cur = conn.cursor()

# 创建表的sql
# sql_create_table = """
#                     create table t_student(
#                         sno int primary key auto_increment,
#                         sname varchar(30) not null,
#                         age tinyint,
#                         score decimal(3,1)
#                     )
# """

# 插入sql
# sql_insert = "insert into t_student(sname,age,score) values(%s,%s,%s)"

# 查询sql
# sql_select = "select * from t_student"

# 修改sql
# sql_update = "update t_student set score=%s where sno=%s"

# 删除sql
sql_delete = "delete from t_student where sno=%s"
# 执行创建表的sql
try:
    # cur.execute(sql_create_table)

    # cur.execute(sql_insert, ('wen1', 18, 90))
    # cur.executemany(sql_insert, [('wen2', 19, 80), ('wen3', 15, 70), ('wen4', 16, 60)])
    # conn.commit()
    # cur.execute(sql_select)
    # one = cur.fetchone()
    # many = cur.fetchall()
    # print(one)
    # print(many)

    # cur.execute(sql_update, (88, 2))
    # conn.commit()
    cur.execute(sql_delete, (2,))
    conn.commit()
    print('创建表成功')
except Exception as e:
    print(e)
    conn.rollback()
    print('创建表失败')
finally:
    conn.close()
