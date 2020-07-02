import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import re

from pandas import read_csv #暂定采用pandas库的导入和清洗函数
filename='./donghang.csv' #csv名称尽量设成英文
f=open(filename,encoding='utf-8') #encoding格式有待商榷 #utf-8，gbk，还有utf-8-sig
names=['始发地','目的地','所在航空公司','航班号','始发机场','目的机场','起飞时间','落地时间','机票价格','数据来源']
data=read_csv(f,names=names)
#print(data)
#data = pd.read_csv(r"donghang.csv", header = None, names=['始发地','目的地','所在航空公司','航班号','始发机场','目的机场','起飞时间','落地时间','机票价格','数据来源'], sep=",")
#print(data)

#data.replace(data.loc[i, '起飞时间'],'0',inplace=True)

dongfang_hk = re.compile('.*直达*')
for i in data['落地时间']._stat_axis.values : # 根据行号遍历dataframe
    item = data.loc[i,'落地时间'] # python中如何找到某特定单元格的内容
    if (re.match(dongfang_hk, item) != None): # python中函数返回为空是等于None
        data.loc[i, '起飞时间'] = data.loc[i, '始发机场']
        data.loc[i, '落地时间'] = data.loc[i, '目的机场']
        data.loc[i, '始发机场'] = "虹桥国际机场"
        data.loc[i, '目的机场'] = "白云机场"

data["目的机场"]="白云机场"
#shoukong_jg = re.compile(x)
for i in data['机票价格']._stat_axis.values : # 根据行号遍历dataframe
    item = data.loc[i,'机票价格'] # python中如何找到某特定单元格的内容
    if (len(item) < 2): # python中函数返回为空是等于None
        data.loc[i, '机票价格'] = "售完"

data.to_csv(".\donghangNEW.csv")

print(data)
