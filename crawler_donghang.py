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

def donghangcrawler(city1,city2,date_in):
	print("东方航空爬虫开始运行")
	infolist = []
	pricelist = []
	resultlist = []
	cell = {}
	date_in = date_in[0:4] + '-' + date_in[4:6] + '-' + date_in[6:8]
	browser = webdriver.Chrome(executable_path="./webdriver/chromedriver.exe")
	browser.get('http://www.ceair.com/')
	ad = browser.find_element_by_id("appd_wrap_close")
	citya = browser.find_element_by_id("label_ID_0")  # 出发城市
	cityb = browser.find_element_by_id("label_ID_1")  # 到达城市
	date = browser.find_element_by_id("depDt")
	datex = browser.find_element_by_id("deptDtRt")
	search = browser.find_element_by_id("btn_flight_search")  # 查询按钮
	time.sleep(0.5)  # 必须等待页面加载结束后开始操作，否则会被当机器人
	ad.click()  # 关闭广告，会遮挡查询页面
	time.sleep(0.5)
	citya.clear()  # 删除默认输入
	time.sleep(0.5)
	citya.send_keys(city1)
	time.sleep(0.5)
	citya.send_keys(Keys.TAB)
	cityb.send_keys(city2)
	time.sleep(0.5)
	cityb.send_keys(Keys.TAB)
	time.sleep(0.5)
	date.send_keys(Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE,
				Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, date_in)  # 清除默认值重新赋值，不能用clear
	time.sleep(0.5)
	date.send_keys(Keys.TAB)  # 消除弹出菜单
	time.sleep(0.5)
	datex.send_keys(Keys.TAB)  # 消除日历菜单
	time.sleep(0.5)
	search.click()
	time.sleep(3)
	try:
		browser.switch_to.window(browser.window_handles[1])  # 定位到跳转后的查询结果页面
	except BaseException:
		time.sleep(5)
		browser.switch_to.window(browser.window_handles[1])  # 定位到跳转后的查询结果页面

	time.sleep(5)
	info = browser.find_elements_by_xpath("//section[@class='summary']")  # 信息模块组
	price = browser.find_elements_by_xpath("//dd[@data-type='economy']")  # 价格方块组
	if info is None or price is None:
		print("----东航--nodata----")
		return resultlist
	for i in info:
		clean = str(i.text).strip().split() # 解析机票基本信息
		# ['东方航空', '|', 'MU5104|直达|', '09:00', '首都国际机场', 'T2', '直达', '11:15', '虹桥国际机场', 'T2', '02小时15分钟']
		clean.remove('|')
		clean[1] = clean[1].split('|')[0]  # 提取航班号
		infolist.append(clean)
	for j in price:
		clean = str(j.text)
		if clean:
			clean = clean.split()[1]
		else:
			clean = '售完'
		pricelist.append(clean)
	for info_, price_ in zip(infolist, pricelist):
		cell['Airline'] = info_[0]
		cell['FlightNumber'] = info_[1]
		cell['dTime'] = info_[2]
		cell['dAirport'] = info_[3]
		cell['aTime'] = info_[6]
		cell['aAirport'] = info_[7]
		cell['LowestPrice'] = price_
		resultlist.append(cell.copy())
	with open('./data/donghang.csv', 'w', encoding='utf-8') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')
		for i in resultlist:
			writer.writerow([city1, city2, i.get("Airline"), i.get('FlightNumber'), i.get('dAirport'),
							 i.get('aAirport'), i.get('dTime'), i.get('aTime'), i.get('LowestPrice'), '东方航空'])
	csvfile.close()
	print("东方航空爬虫运行结束")
	return resultlist


if __name__=="__main__":
	city1 = "北京"
	city2 = "广州"
	date_in = '20200708'  # 实例格式如 20200706
	a=donghangcrawler(city1, city2, date_in)
	for i in a:
		print(i.values())