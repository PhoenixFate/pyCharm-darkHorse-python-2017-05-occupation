# pip install pymysql
# pip install cryptography
from pymysql import connect


def my_insert():
    # 创建Connection连接
    my_connection = connect(host="114.67.89.253",
                            port=3306,
                            user="root",
                            password="centos123qwer",
                            database="python_darkHorse2017_jingdong", charset="utf8")
    # 获得Cursor对象
    my_cursor = my_connection.cursor()

    # 执行sql，返回受影响的行数
    sql = 'insert into goods(name,cate_name,brand_name) values ("test01","test_cate_name","test_brand_name")'
    count = my_cursor.execute(sql)
    print(count)

    # # 更新
    # count = cs1.execute('update goods_cates set name="机械硬盘" where name="硬盘"')
    # # 删除
    # count = cs1.execute('delete from goods_cates where id=6')

    # 提交之前的操作，如果之前已经之执行过多次的execute，那么就都进行提交
    my_connection.commit()

    # 关闭cursor对象
    my_cursor.close()
    # 关闭Connection对象
    my_connection.close()


def query_one():
    # 创建Connection连接
    my_connection = connect(host="114.67.89.253",
                            port=3306,
                            user="root",
                            password="centos123qwer",
                            database="python_darkHorse2017_jingdong", charset="utf8")
    # 获得Cursor对象
    my_cursor = my_connection.cursor()
    # 执行select语句，并返回受影响的行数：查询一条数据
    count = my_cursor.execute('select * from goods where id>=20')
    # 打印受影响的行数
    print("查询到%d条数据:" % count)

    for i in range(count):
        # 获取查询的结果
        result = my_cursor.fetchone()
        # 打印查询的结果
        print(result)
        # 获取查询的结果

    # 关闭Cursor对象
    my_cursor.close()
    my_connection.close()


def query_all():
    # 创建Connection连接
    my_connection = connect(host="114.67.89.253",
                            port=3306,
                            user="root",
                            password="centos123qwer",
                            database="python_darkHorse2017_jingdong", charset="utf8")
    # 获得Cursor对象
    my_cursor = my_connection.cursor()
    # 执行select语句，并返回受影响的行数：查询一条数据
    count = my_cursor.execute('select * from goods where id>=10')
    # 打印受影响的行数
    print("查询到%d条数据:" % count)

    result = my_cursor.fetchall()
    print(result)

    # 关闭Cursor对象
    my_cursor.close()
    my_connection.close()


def main():
    # my_insert()
    query_one()
    query_all()


if __name__ == '__main__':
    main()
