# -*- coding:utf-8 -*-
import MySQLdb
db = MySQLdb.connect("localhost","root","","recommend")
cursor = db.cursor()
sql = "create table user_admin(user int, anime int)"
cursor.execute(sql)
db.close()