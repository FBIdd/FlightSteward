#%%
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mysql.connector

config ={
    'user':'root',        #用户名
    'passwd':'111111',   #自己设定的密码
    'host':'localhost'   #ip地址，本地填127.0.0.1，也可以填localhost
}

mydb = mysql.connector.connect(**config)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
flag=0  #判断database是否存在的标志
for x in mycursor:
    #print(x)
    if x[0]=='flights':
        flag=1
if flag==1:     #database存在->直接使用
    mycursor.execute("USE flights")
elif flag==0:   #database不存在->建立database及tables
    mycursor.execute("CREATE DATABASE flights")
    mydb.commit()
    mycursor.execute("USE flights")
    mycursor.execute("CREATE TABLE flight (ptmc VARCHAR(255), hbh VARCHAR(255))")
mydb.commit()       #数据表内容有更新

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

print("down")