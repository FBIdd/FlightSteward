import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts

def price_view_dongfang():
    pr = pd.read_csv("G:/Git/Git/flightsteward/FlightSteward/data/donghangNEW.csv")
    #print(pr)
    number = pr["航班号"].tolist()
    price = pr["机票价格"].tolist()
    #print(price)

    bar = Bar()
    bar.add_xaxis(number)
    bar.add_yaxis("机票价格",price)
    bar.set_global_opts(title_opts=opts.TitleOpts(title="东方航空各航班价格",subtitle="上海-广州"))
    bar.render('donghang_price.html')



if __name__ == "__main__":
    price_view_dongfang()
