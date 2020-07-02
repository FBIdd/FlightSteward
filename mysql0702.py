# %%
# !/usr/bin/python
# -*- coding: UTF-8 -*-

import mysql.connector
import pandas as pd
import numpy as np
from pandas import DataFrame,Series
from pandas import read_csv

config = {
    'user': 'root',  # 用户名
    'passwd': '111111',  # 自己设定的密码
    'host': 'localhost'  # ip地址，本地填127.0.0.1，也可以填localhost
}

mydb = mysql.connector.connect(**config)
#print(mydb)
mycursor = mydb.cursor()
#mycursor.execute("SHOW DATABASES")

def create_database(): #建立数据库
    flag = 0  # 判断database是否存在的标志
    for x in mycursor:
        # print(x)
        if x[0] == 'flight':
            flag = 1
    if flag == 1:  # database存在->直接使用
        mycursor.execute("USE flight")
    elif flag == 0:  # database不存在->建立database及tables
        mycursor.execute("CREATE DATABASE flight")
        mydb.commit()
        mycursor.execute("USE flight")
        mycursor.execute("CREATE TABLE maindata (sfd VARCHAR(5),mdd VARCHAR(5),hkgs VARCHAR(10),hbh VARCHAR(10),sfjc VARCHAR(10),ddjc VARCHAR(10),qfsj VARCHAR(5),ddsj VARCHAR(5),jpjg VARCHAR(5),july VARCHAR(10))")
        mycursor.execute("CREATE TABLE donghang (sfd VARCHAR(5),mdd VARCHAR(5),hkgs VARCHAR(10),hbh VARCHAR(10),sfjc VARCHAR(10),ddjc VARCHAR(10),qfsj VARCHAR(5),ddsj VARCHAR(5),jpjg VARCHAR(5),july VARCHAR(10))")
        mycursor.execute("CREATE TABLE lianhang (sfd VARCHAR(5),mdd VARCHAR(5),hkgs VARCHAR(10),hbh VARCHAR(10),sfjc VARCHAR(10),ddjc VARCHAR(10),qfsj VARCHAR(5),ddsj VARCHAR(5),jpjg VARCHAR(5),july VARCHAR(10))")
        mycursor.execute("CREATE TABLE jixiang (sfd VARCHAR(5),mdd VARCHAR(5),hkgs VARCHAR(10),hbh VARCHAR(10),sfjc VARCHAR(10),ddjc VARCHAR(10),qfsj VARCHAR(5),ddsj VARCHAR(5),jpjg VARCHAR(5),july VARCHAR(10))")
        mycursor.execute("CREATE TABLE nanhang (sfd VARCHAR(5),mdd VARCHAR(5),hkgs VARCHAR(10),hbh VARCHAR(10),sfjc VARCHAR(10),ddjc VARCHAR(10),qfsj VARCHAR(5),ddsj VARCHAR(5),jpjg VARCHAR(5),july VARCHAR(10))")
    mydb.commit()  # 数据表内容有更新
    mycursor.execute("SHOW TABLES")
    #for x in mycursor:
        #print(x)

def insert(data,table): #将数据插入表中
    sql="INSERT INTO "+table+" (sfd,mdd,hkgs,hbh,sfjc,ddjc,qfsj,ddsj,jpjg,july) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=data
    mycursor.execute(sql,val)
    mydb.commit()

def findAll(table): #查看整个表
    print("查看所有数据")    #执行SQL 不带参数的查询语句
    command="select * from "+table
    mycursor.execute(command)     #获取所有记录
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    print("")

def find(sth,table): #取特定列
    print("查看%s表中%s列的数据："%(table,sth))
    command="select "+sth+" from "+table
    mycursor.execute(command)  # 获取所有记录
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    print("")

def create_table(table): #将数据导入表中
    file = table+".csv"
    fo = open(file, encoding='UTF-8')
    data = read_csv(fo)
    a_line = data.values.tolist()
    print(a_line)
    for i in a_line:
        insert(i, table)
    mydb.commit()

create_database()
create_table('maindata')
create_table('donghang')
create_table('lianhang')
create_table('jixiang')
create_table('nanhang')


"""findAll('maindata')
find('hbh','maindata')
print("done")"""