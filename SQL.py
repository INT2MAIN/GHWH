# 提供于数据库相关的操作方法
import pymysql

def execute_sql(sql):
    # 连接数据库
    db = pymysql.connect("192.168.0.7:1435", "YDHIS", "sa", "jtzx@2019,.")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)
    # 使用 fetchall() 方法获取所有数据
    data = cursor.fetchall()
    #     print(data)
    # 关闭数据库连接
    db.close()
    # 返回数据内容
    return data

sql="select * from YDHIS..T_MZFYMXWSF_02 with(nolock) where CMZH = '2003000192' and CJGID = 48 and isnull(BBKSF, 0) = 0"
a=execute_sql(sql)
print(a)
if __name__ == "__main__":
    print('123')

