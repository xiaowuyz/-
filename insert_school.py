#codeing
import requests
from time import sleep
from time import time
from city import city
import pymysql
configmodel = {
    'host': 'xiaowufangwen.mysql.rds.aliyuncs.com',
    'port': 3306,
    'user': 'root',
    'password': 'Wyz472069886',
    'db': 'test',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}
configcorapi = {
    'host': 'xiaowufangwen.mysql.rds.aliyuncs.com',
    'port': 3306,
    'user': 'root',
    'password': 'Wyz472069886',
    'db': 'co',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}
def timestamp():
    """
    当前时间时间戳
    :return:
    """
    return int(time())
def conn(sql, config):
    connection = pymysql.connect(**config)
    with connection.cursor() as cursor:
        cursor.execute(sql)
        q = cursor.fetchall()
    connection.commit()
    connection.close()
    return q
def insert(date, code):
    for i in date:
        print(code, i['name'])
        t = timestamp()
        sql_insert = r"INSERT INTO `co`.`school` (`name`, `code`, `created_time`, `updated_time`, `deleted`) VALUES ('{}', '{}', '{}', '{}', '0');". \
            format(i['name'], code, t, t)
        while 1:
            try:
                conn(sql_insert, configcorapi)
                break
            except Exception as e:
                print(e)
                print('sql', sql)
                pass
for i in city:
    for j in i['cities']:
        if 'cities' in j:
            for k in j['cities']:
                while 1:
                    try:
                        sql = r"SELECT name FROM test.school where region = '{}';".format(k['code'])
                        data = conn(sql, configmodel)
                        insert(data, k['code'])
                        break
                    except Exception as e:
                        print(e)
                        print('sql', sql)
                        pass
        else:
            while 1:
                try:
                    sql = r"SELECT name FROM test.school where region = '{}';".format(j['code'])
                    data = conn(sql, configmodel)
                    insert(data, j['code'])
                    break
                except Exception as e:
                    print(e)
                    print('sql', sql)
                    pass