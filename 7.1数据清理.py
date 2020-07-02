import pandas as pd
import numpy as np
from pandas import DataFrame,Series

from pandas import read_csv #暂定采用pandas库的导入和清洗函数
filename=input("文件名：") #csv名称尽量设成英文
f=open(filename,encoding='UTF-8') #encoding格式有待商榷 #utf-8，gbk，还有utf-8-sig
names=['航班号','机型','所在航空公司','始发地','目的地','起飞时间','航班时间','机票价格','数据来源']
data=read_csv(f,names=names)
print(data)

df['机票价格'] = df['机票价格'].str.split(str=",") #将机票价格这一列的数据根据“，”分割成数组
df['机票价格'] = df['机票价格'].astype(np.float64) #将机票价格列的数据形式转化成浮点数格式
df['机票价格'] = df['机票价格'].astype(np.float64) #取机票价格中最大的值
data.[7:1] = min(enumerate(data.[7:1]), key=operator.itemgetter(1)) #取机票价格中最小的

data[u'机票价格'][(data[u'机票价格']<0) | (data[u'机票价格']>100000)] = None #将异常值清空
print(data.dropna()) #清空后删除
#print("---------------------------------\n显示每一列中有多少个缺失值：\n",data.isnull().sum())
#返回每列包含的缺失值的个数
data.dropna(subset = [u'机票价格']) #判断价格列，如果价格列信息缺失就删除这行
#print(examDf.duplicated()) #判断是否有重复行，重复的显示为TRUE，
examDf.drop_duplicates() #去掉完全重复的行
