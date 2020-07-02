import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts

def price_view_xiecheng():
    #这里的文件是从本地读取的
    pr = pd.read_csv("G:/Git/Git/flightsteward/FlightSteward/data/maindata.csv")
    #下面两行是将相应数据转换为列表
    number = pr["航班号"].tolist()
    price = pr["机票价格"].tolist()

    bar = Bar()
    bar.add_xaxis(number)
    bar.add_yaxis("机票价格",price)
    bar.set_global_opts(title_opts=opts.TitleOpts(title="携程上各航班价格",subtitle="上海-广州"))
    #最后保存为一个网页文件
    bar.render('price.html')


if __name__ == "__main__":
    price_view_xiecheng()
