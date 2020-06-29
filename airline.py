from mainspider_post import getdata, message
import time
import random

# 一个子程序用于确定在爬虫范围内的航空公司名单
airline = []
data = []
city = ['北京', '上海', '广州']
for i in city:
	for j in city:
		if i is not j:
			for date in range(20200706, 20200720):
				print(i, j)
				data = data + list(message(getdata(i, j, str(date))))
				time.sleep(random.random()*30)  # 随机休眠时间而且比较长，过于规律会被禁封
for i in data:
	if i['AirLine'] not in airline:
		airline.append(i['AirLine'])
print(airline)