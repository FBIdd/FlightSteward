import mainspider_post
from crawler_donghang import donghangcrawler
from crawler_jixiang import jixiangcrawler
from crawler_lianhang import lianhangcrawler
from multiprocessing import Process

if __name__ == "__main__":
	dcity = input("请选择出发城市(北京、上海、广州): ")
	acity = input("请选择到达城市(北京、上海、广州): ")
	date = input("请输入日期('20200706'): ")
	airline = mainspider_post.message(mainspider_post.getdata(dcity, acity, date), dcity, acity, date)
	print(airline)
	#  获取航空公司名单（已经去重），爬取携程票据
	#  定义爬虫进程
	csvlist = []
	donghangPro = Process(target=donghangcrawler, args=(dcity, acity, date))
	jixiangPro = Process(target=jixiangcrawler, args=(dcity, acity, date))
	lianhangPro = Process(target=lianhangcrawler, args=(dcity, acity, date))
	for i in airline:
		if i == '东方航空':
			print('定位到东方航空')
			donghangPro.start()
			donghangPro.join()
			csvlist.append(["donghang.csv"])
		elif i == '吉祥航空':
			print('定位到吉祥航空')
			jixiangPro.start()
			csvlist.append("jixiang.csv")
			print("吉祥航空爬虫开始运行")
		elif i == '中国联合航空':
			print('定位到中国联合航空')
			lianhangPro.start()
			csvlist.append("lianghang.csv")
			print("中国联合航空爬虫开始运行")
	for i in airline:  # 主进程阻塞等待子进程完成
		if i == '吉祥航空':
			jixiangPro.join()
		elif i == '中国联合航空':
			lianhangPro.join()

print('项目执行完成')