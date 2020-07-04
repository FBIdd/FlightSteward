from selenium import webdriver
import time
import csv
import  selenium
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# 不能广州到上海
def lianhangcrawler(city1,city2,date_in):
	print("中国联合航空爬虫开始运行")
	flightlist = []
	pricelist = []
	resultlist = []
	dairportlist=[]
	dtimelist=[]
	atimelist=[]
	aairportlist=[]
	cell = {}
	date_in = date_in[0:4] + '-' + date_in[4:6] + '-' + date_in[6:8]
	browser = webdriver.Firefox(executable_path="./webdriver/geckodriver.exe")
	browser.get('http://www.flycua.com/')
	citya = browser.find_element_by_id("_easyui_textbox_input1")
	cityb = browser.find_element_by_id("_easyui_textbox_input2")
	date = browser.find_element_by_id("departDate")
	search = browser.find_element_by_xpath("//div[@class='search-btn']") # 查询按钮
	time.sleep(0.5)
	citya.clear()
	time.sleep(0.5)
	citya.click()  # 弹出城市选择
	time.sleep(0.5)
	button = browser.find_elements_by_xpath("//li[@code]")
	for i in button:  # 找到指定出发城市城市的选择按钮
		if str(i.text) == city1:
			i.click()
	time.sleep(1)
	button = browser.find_elements_by_xpath("//li[@code]")
	for i in button:  # 找到指定到达城市城市的选择按钮
		if str(i.text) == city2:
			i.click()
	time.sleep(1)
	date.click()
	time.sleep(1)
	strmonth = str(int(date_in[5:7])-1)  # 这网页很奇怪，月份属性数值比实际的小1
	datebutton = browser.find_elements_by_xpath("//td[@data-month='" + strmonth+"']")
	try:
		for i in datebutton:  # 找到指定到达城市城市的选择按钮
			if str(i.text) == str(int(date_in[8:10])):
				i.click()
	except selenium.common.exceptions.StaleElementReferenceException:
		print('=====well=====')
	print('----------------------')
	time.sleep(0.5)
	search.click()
	time.sleep(5)
	flightdata = browser.find_elements_by_xpath("//span[@class='flight-number']")
	if flightdata is None:
		print("----------吉祥航空--No data---------")
		return resultlist
	dcitydata = browser.find_elements_by_xpath("//li[@class='flightList_item_departureInfo']")
	acitydata= browser.find_elements_by_xpath("//li[@class='flightList_item_arrivalInfo']")
	pricedata = browser.find_elements_by_xpath("//span[@class='flightPrice']")
	lenth= len(pricedata)
	for i in flightdata:
		print(i.text)
	for i in dcitydata:
		print(i.text)
	for i in acitydata:
		print(i.text)
	for i in pricedata:
		print(i.text)

	for i in range(lenth):
		flightlist.append(str(flightdata[i].text).split('|')[0].strip())
		dtimelist.append(str(dcitydata[i].text).split()[1])
		dairportlist.append(str(dcitydata[i].text).split()[2])
		atimelist.append(str(acitydata[i].text).split()[1])
		aairportlist.append(str(acitydata[i].text).split()[2])
		pricelist.append(str(pricedata[i].text))

	for i in range(lenth):
		cell['Airline'] = "中国联合航空"
		cell['FlightNumber'] = flightlist[i]
		cell['dTime'] = dtimelist[i]
		cell['dAirport'] = dairportlist[i]
		cell['aTime'] = atimelist[i]
		cell['aAirport'] = aairportlist[i]
		cell['LowestPrice'] = pricelist[i]
		resultlist.append(cell.copy())
	with open('./data/lianhang.csv', 'w', encoding='utf-8') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')
		for i in resultlist:
			writer.writerow([city1, city2, i.get("Airline"), i.get('FlightNumber'), i.get('dAirport'),
							 i.get('aAirport'), i.get('dTime'), i.get('aTime'), i.get('LowestPrice'), '中国联合航空'])
	csvfile.close()
	print("中国联合航空航空爬虫运行结束")
	return resultlist

if __name__=="__main__":
	city1 = "上海"
	city2 = "北京"
	date_in = '20200717'  # 实例格式如 20200706
	a=lianhangcrawler(city1, city2, date_in)
	for i in a:
		print(i.values())