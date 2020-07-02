import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import re

from pandas import read_csv
filename='./jixiang.csv'
f=open(filename,encoding='utf-8')
names=['始发地','目的地','所在航空公司','航班号','始发机场','目的机场','起飞时间','落地时间','机票价格','数据来源']
data=read_csv(f,names=names)

data["始发机场"]="虹桥国际机场"
data["目的机场"]="白云机场"

data.to_csv(".\jixiangNEW.csv")

print(data)