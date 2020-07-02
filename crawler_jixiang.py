from selenium import webdriver
import time
import csv
import copy
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import actions

# 只能上海到广州
def jixiangcrawler(city1,city2,date_in):
	flightlist = []
	pricelist = []
	resultlist = []
	dairportlist=[]
	dtimelist=[]
	atimelist=[]
	aairportlist=[]
	cell = {}
	date_in = date_in[0:4] + '-' + date_in[4:6] + '-' + date_in[6:8]
	browser = webdriver.Chrome(executable_path="./webdriver/chromedriver.exe")
	browser.get('http://www.juneyaoair.com/')
	citya = browser.find_element_by_id("fromcity")  # 出发城市
	cityb = browser.find_element_by_id("tocity")  # 到达城市
	date = browser.find_element_by_id("date01")
	search = browser.find_element_by_id("boxs-left-img-search")  # 查询按钮
	time.sleep(0.5)  # 必须等待页面加载结束后开始操作，否则会被当机器人
	ad = browser.find_element_by_xpath("//div[@class='g-sliderTwo']")
	ad.click()  # 去除广告
	citya.clear()  # 删除默认输入
	time.sleep(0.5)
	citya.click()  # 弹出城市选择
	time.sleep(0.5)
	button = browser.find_elements_by_id("selectedCity")
	for i in button:  # 找到指定出发城市城市的选择按钮
		if str(i.text)==city1:
			i.click()
	time.sleep(1)
	button = browser.find_elements_by_id("selectedCity")
	for i in button:  # 找到指定到达城市城市的选择按钮
		if str(i.text) == city2:
			i.click()
	time.sleep(1)
	cityb.send_keys(Keys.TAB)
	time.sleep(1)
	date.send_keys(Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE,
				Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, date_in)  # 清除默认值重新赋值，不能用clear
	time.sleep(0.5)
	search.click()
	time.sleep(5)
	flightdata = browser.find_elements_by_xpath("//div[@class='flt_No']")
	if flightdata is None:
		print("----------吉祥航空--No data---------")
		return resultlist
	dcitydata = browser.find_elements_by_xpath("//div[@class='flt_from']")
	acitydata= browser.find_elements_by_xpath("//div[@class='flt_to']")
	pricedata = browser.find_elements_by_xpath("//div[@class='flt_price']")
	lenth= len(pricedata)

	for i in range(lenth):
		flightlist.append(str(flightdata[i].text))
		dtimelist.append(str(dcitydata[i].text).split()[0])
		dairportlist.append(str(dcitydata[i].text).split()[1])
		atimelist.append(str(acitydata[i].text).split()[0])
		aairportlist.append(str(acitydata[i].text).split()[1])
		pricelist.append(str(pricedata[i].text)[1:-1])

	for i in range(lenth):
		cell['Airline'] = "吉祥航空"
		cell['FlightNumber'] = flightlist[i]
		cell['dTime'] = dtimelist[i]
		cell['dAirport'] = dairportlist[i]
		cell['aTime'] = atimelist[i]
		cell['aAirport'] = aairportlist[i]
		cell['LowestPrice'] = pricelist[i]
		resultlist.append(cell.copy())
	with open('./data/jixiang.csv', 'w', encoding='utf-8') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')
		for i in resultlist:
			writer.writerow([city1, city2, i.get("Airline"), i.get('FlightNumber'), i.get('dAirport'),
							 i.get('aAirport'), i.get('dTime'), i.get('aTime'), i.get('LowestPrice'), '吉祥航空'])
	csvfile.close()

	return resultlist


if __name__=="__main__":
	city1 = "上海"
	city2 = "广州"
	date_in = '20200706'  # 实例格式如 20200706
	a=jixiangcrawler(city1, city2, date_in)
	for i in a:
		print(i.values())