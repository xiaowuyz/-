#!/usr/bin/env python3
import requests
from time import sleep
from citys import city
import pymysql
config = {
          'host': 'xiaowufangwen.mysql.rds.aliyuncs.com',
          'port': 3306,
          'user': 'root',
          'password':'Wyz472069886',
          'db':'test',
          'charset':'utf8',
          'cursorclass':pymysql.cursors.DictCursor,
          }
def conn(sql):
    connection = pymysql.connect(**config)
    with connection.cursor() as cursor:
        cursor.execute(sql)
        q = cursor.fetchall()
    connection.commit()
    connection.close()
    return q
def school(id):
    url = r'http://ucenter.17zuoye.com/school/areaschoolrs.api?regions={}&level=PRIMARY_SCHOOL'.format(id)
    sql_valid = r"SELECT count(*) as n FROM test.school where region = '{}';".format(id)
    an = conn(sql_valid)
    if an[0]['n'] == 0:
        req = requests.get(url).json()
        print("url", url)
        for i in req['rows']:
            print("s", i['name'])
            while 1:
                try:
                    sql = r"INSERT INTO `test`.`school` (`region`, `name`, `school_id`) VALUES ('{}', '{}', '{}');".format(i['region'], i['name'], i['id'])
                    conn(sql)
                    break
                except Exception as e:
                    print(e)
                    print('sql', sql)
                    pass

for i, items in city.items():
    for j in items:
        # print(j)
        if j['state'] == 'closed':
            for k in j['citys']:
                school(k['id'])
        else:
            print("j", j['id'])
            school(j['id'])