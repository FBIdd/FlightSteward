import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import re

#清洗东方航空
from pandas import read_csv
filename='./donghang.csv'
f=open(filename,encoding='utf-8')
names=['始发地','目的地','所在航空公司','航班号','始发机场','目的机场','起飞时间','落地时间','机票价格','数据来源']
dataDF=read_csv(f,names=names)

dongfang_hk = re.compile('.*直达*')
for i in dataDF['落地时间']._stat_axis.values :
    item = dataDF.loc[i,'落地时间']
    if (re.match(dongfang_hk, item) != None):
        dataDF.loc[i, '起飞时间'] = dataDF.loc[i, '始发机场']
        dataDF.loc[i, '落地时间'] = dataDF.loc[i, '目的机场']
        dataDF.loc[i, '始发机场'] = "虹桥国际机场"
        dataDF.loc[i, '目的机场'] = "白云机场"

dataDF["目的机场"]="白云机场"
for i in dataDF['机票价格']._stat_axis.values :
    item = dataDF.loc[i,'机票价格']
    if (len(item) < 2):
        dataDF.loc[i, '机票价格'] = "售完"

dataDF.to_csv(".\donghangNEW.csv")
print(dataDF)

#清洗吉祥航空
from pandas import read_csv
filename='./jixiang.csv'
f=open(filename,encoding='utf-8')
names=['始发地','目的地','所在航空公司','航班号','始发机场','目的机场','起飞时间','落地时间','机票价格','数据来源']
dataJX=read_csv(f,names=names)

hongqiao_up = re.compile('.*虹桥*')
for i in dataJX['始发机场']._stat_axis.values :
    item = dataJX.loc[i,'始发机场']
    if (re.match(hongqiao_up, item) != None):
        dataJX.loc[i, '始发机场'] = "虹桥国际机场"

baiyun_up = re.compile('.*白云*')
for i in dataJX['始发机场']._stat_axis.values :
    item = dataJX.loc[i,'始发机场']
    if (re.match(baiyun_up, item) != None):
        dataJX.loc[i, '始发机场'] = "白云机场"

baiyun_down= re.compile('.*白云*')
for i in dataJX['目的机场']._stat_axis.values :
    item = dataJX.loc[i,'目的机场']
    if (re.match(baiyun_down, item) != None):
        dataJX.loc[i, '目的机场'] = "白云机场"

hongqiao_down= re.compile('.*虹桥*')
for i in dataJX['目的机场']._stat_axis.values :
    item = dataJX.loc[i,'目的机场']
    if (re.match(hongqiao_down, item) != None):
        dataJX.loc[i, '目的机场'] = "虹桥国际机场"

dataJX.to_csv(".\jixiangNEW.csv")
print(dataJX)