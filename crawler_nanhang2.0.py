from selenium import webdriver
import time
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def nanhangcrawler(city1,city2,date_in):
	date_in = date_in[0:4] + '-' + date_in[4:6] + '-' + date_in[6:8]
	option = ChromeOptions()
	option.add_experimental_option('excludeSwitches', ['enable-automation'])
	browser = webdriver.Chrome(executable_path="./webdriver/chromedriver.exe",options=option)
	browser.get('https://www.csair.com/cn/')
	script = 'Object.defineProperty(navigator,"webdriver",{get:() => false,});'
	# 运行Javascript
	browser.execute_script(script)
	citya = browser.find_element_by_id("fDepCity")  # 出发城市
	cityb = browser.find_element_by_id("fArrCity")  # 到达城市
	date = browser.find_element_by_id("fDepDate")  # 日期不能直接输入，需要等待生成选择界面
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
	time.sleep(2)
	search.click()
	time.sleep(10)
	data = browser.find_element_by_class_name("zls-flg-ui")  # 查询结果动态生成的UI表格
	for i in data:
		cell = str(i.text)  # 包含所需信息的字符串,结果待处理
		print(cell)
	return data

if __name__=="__main__":
	city1 = "上海"
	city2 = "北京"
	date_in = "20200706"
	print(nanhangcrawler(city1, city2, date_in))



