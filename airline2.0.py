from mainspider_post import getdata, message
import time
import random
import copy

# 尝试乱序的爬取方式
order = {}
tool = {}
orderlist = []
rlist = []
data = []
oneline = {}
city = ['北京', '上海', '广州']

for i in city:
	for j in city:
		if i is not j:
			for date in range(20200706, 202007015):
				order['city1'] = i
				order['city2'] = j
				order['date'] = str(date)
				tool = copy.copy(order)
				orderlist.append(tool)  # 初始指令池
random.shuffle(orderlist)  # 随机排序

for od in orderlist:
	print(od.values())
	data = list(message(getdata(od['city1'], od['city2'], str(od['date']))))
	for i in data:
		if i['Airline'] not in rlist:
			rlist.append(i['Airline'])  # 添加新的公司到名单
	time.sleep(random.random() * 30)  # 随机休眠时间而且比较长，过于规律会被禁封
print(rlist)

# ['南方航空', '东方航空', '上海航空', '海南航空', '中国国航', '吉祥航空', '金鹏航空', '春秋航空', '厦门航空', '中国联合航空', '天津航空']

