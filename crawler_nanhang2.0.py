from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def nanhangcrawler(city1,city2,date_in):
	date_in = date_in[0:4] + '-' + date_in[4:6] + '-' + date_in[6:8]
	browser = webdriver.Chrome(executable_path="./webdriver/chromedriver.exe")
	browser.get('https://www.csair.com/cn/')
	citya = browser.find_element_by_id("fDepCity")  # 出发城市
	cityb = browser.find_element_by_id("fArrCity")  # 到达城市
	date = browser.find_element_by_id("fDepDate")
	search = browser.find_element_by_class_name("fr.searchBtn.searchFlight")  # 查询按钮

	citya.send_keys(city1)
	time.sleep(1)
	cityb.send_keys(city2)
	time.sleep(1)
	date.click()
	# WebDriverWait(browser, 5).until(expected_conditions.presence_of_all_elements_located(By.CLASS_NAME, "cld-ceil"))
	# 等待页面反应，加载日历,使用webdriverwait设置等待，没调通
	time.sleep(1.5)
	datebox = browser.find_element_by_xpath("//li[@data-value=" + "'" + date_in + "']")
	datebox.click()
	search.click()
	time.sleep(10)
	data = browser.find_element_by_class_name("zls-flg-ui")  # 查询结果动态生成的UI表格
	data = data.text  # 包含所需信息的字符串,结果待处理
	return data

if __name__=="__main__":
	city1 = input("输入出发城市：")
	city2 = input("输入到达城市：")
	date_in = input("输入日期")  # 实例格式如 20200706
	print(nanhangcrawler(city1, city2, date_in))



