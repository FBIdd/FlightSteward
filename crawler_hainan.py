from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def nanhangcrawler(city1,city2,date_in):
	date_in = date_in[0:4] + '-' + date_in[4:6] + '-' + date_in[6:8]
	browser = webdriver.Firefox(executable_path="./webdriver/geckodriver.exe")
	browser.get('https://www.hnair.com/')
	citya = browser.find_element_by_id("from_city1")  # 出发城市
	cityb = browser.find_element_by_id("to_city1")  # 到达城市
	date = browser.find_element_by_id("flightBeginDate1")  # 日期不能直接输入，需要等待生成选择界面
	search = browser.find_element_by_class_name("btn-search")  # 查询按钮
	icon = browser.find_element_by_id("onlyDirectId")  # 选择按钮
	time.sleep(1)
	citya.clear()
	citya.send_keys(city1)
	time.sleep(1)
	cityb.send_keys(city2)
	time.sleep(1)
	date.click()
	# WebDriverWait(browser, 5).until(expected_conditions.presence_of_all_elements_located(By.CLASS_NAME, "cld-ceil"))
	# 等待页面反应，加载日历,使用webdriverwait设置等待，没调通
	time.sleep(1.5)
	date.clear()
	date.send_keys(date_in)
	icon.click()  # 选择只看直飞航班的选择按钮
	time.sleep(1)
	tip = ActionChains(browser)
	tip.move_to_element(search).perform()
	time.sleep(0.5)
	tip.context_click(search).perform()
	time.sleep(10)
	data = 1
	return data

if __name__=="__main__":
	city1 = "上海虹桥"
	city2 = "北京首都"
	date_in = "20200706"  # 实例格式如 20200706
	print(nanhangcrawler(city1, city2, date_in))

