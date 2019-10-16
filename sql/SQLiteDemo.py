import sqlite3

# 链接数据库
conn = sqlite3.connect('E:/python/DB/demo.db')

# 创建游标对象
cur = conn.cursor()

# # 创建表的sql语句
# sql = """create table t_person (
#             pno integer primary key autoincrement,
#             pname varchar not null ,
#             age integer
# )"""

# 插入数据
# sql = "insert into t_person(pname,age) values(?,?)"

# 查询数据
sql = "select * from t_person"

# 修改数据
# sql = 'update t_person set pname=? where pno=?'

# 删除数据
sql_delete = 'delete from t_person where pno=?'
# 执行SQL语句

try:
    # cur.execute(sql)
    # print('创建表成功')

    # # 插入单条数据
    # cur.execute(sql, ('wen', '20'))

    # # 插入多条语句
    # cur.executemany(sql, [('wen1', 20), ('wen2', 30), ('wen4', 40)])
    # 提交事务
    # conn.commit()

    cur.execute(sql)
    #
    # # 获取查询结果集
    # fetchone = cur.fetchone()
    # print(fetchone)
    # fetchall = cur.fetchall()
    # print(fetchall)
    # print('创建数据成功')

    # cur.execute(sql, ('你好', 2))
    # conn.commit()

    # 删除
    # cur.execute(sql_delete, (1,))
    # conn.commit()

    # 获取查询结果集
    fetchone = cur.fetchone()
    print(fetchone)
    fetchall = cur.fetchall()
    print(fetchall)


except Exception as e:
    print(e)
    # conn.rollback()
    print('创建表失败')
finally:
    # 关闭游标
    cur.close()
    # 关闭链接
    conn.close()
