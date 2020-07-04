import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import re

#北京--广州
#清洗东方航空
from pandas import read_csv
filename='./donghangB-G.csv'
f=open(filename,encoding='gbk')
names=['始发地','目的地','所在航空公司','航班号','始发机场','目的机场','起飞时间','落地时间','机票价格','数据来源','日期']
dataDF=read_csv(f,names=names)

#1.
jingting = re.compile('.*经停*')
for i in dataDF['落地时间']._stat_axis.values :
    item = dataDF.loc[i,'落地时间']
    if (re.match(jingting, item) != None):
        dataDF.loc[i, '起飞时间'] = dataDF.loc[i, '目的机场']
        dataDF.loc[i, '落地时间'] = dataDF.loc[i, '起飞时间']
        dataDF.loc[i, '目的机场'] = "白云机场"

#2.
zhida = re.compile('.*直达*')
for i in dataDF['落地时间']._stat_axis.values :
    item = dataDF.loc[i,'落地时间']
    if (re.match(zhida, item) != None):
        dataDF.loc[i, '起飞时间'] = dataDF.loc[i, '目的机场']
        dataDF.loc[i, '落地时间'] = dataDF.loc[i, '起飞时间']
        dataDF.loc[i, '始发机场'] = "首都国际机场"
        dataDF.loc[i, '目的机场'] = "白云机场"

#3.
yitian = re.compile('.*1天*')
for i in dataDF['目的机场']._stat_axis.values :
    item = dataDF.loc[i,'目的机场']
    if (re.match(yitian, item) != None):
        dataDF.loc[i, '目的机场'] = "白云机场"

#4.
T1= re.compile('.*T1*')
for i in dataDF['目的机场']._stat_axis.values :
    item = dataDF.loc[i,'目的机场']
    if (re.match(yitian, item) != None):
        dataDF.loc[i, '目的机场'] = "白云机场"
        dataDF.loc[i, '落地时间'] = "未知"

#5.
baiyun= re.compile('.*白云机场*')
for i in dataDF['落地时间']._stat_axis.values :
    item = dataDF.loc[i,'落地时间']
    if (re.match(baiyun, item) != None):
        dataDF.loc[i, '落地时间'] = "未知"

dataDF.to_csv(".\dongfangB-GNEW.csv")

#清洗联航
from pandas import read_csv
filename='./lianhangB-G.csv'
f=open(filename,encoding='gbk')
names=['始发地','目的地','所在航空公司','航班号','始发机场','目的机场','起飞时间','落地时间','机票价格','数据来源','日期']
dataLH=read_csv(f,names=names)

#1.
jiayi = re.compile('.*1*')
for i in dataDF['目的机场']._stat_axis.values :
    item = dataDF.loc[i,'目的机场']
    if (re.match(jiayi, item) != None):
        dataDF.loc[i, '目的机场'] = "佛山沙提机场"

dataDF.to_csv(".\lianhangB-GNEW.csv")
print(dataLH)