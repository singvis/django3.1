#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

import pymysql
from django.utils import timezone

"""数据库连接测试"""

# 创建连接
conn = pymysql.Connect(host='192.168.8.130',
                       user='root',
                       password='DevOps@2020',
                       port=3306,
                       database='django_db')
# 创建游标
cur = conn.cursor()

print(cur)

# 关闭游标
cur.close()
# 关闭连接
conn.close()



# print(timezone.datetime.date())