from pyecharts import options as opts
import pandas
from pyecharts.charts import Bar, Timeline, Page, Line
from pyecharts.globals import ThemeType
from pyecharts.components import Table
def visual(start,end,airlinelist):
    show = Page()
    Df = pandas.read_csv('.\data\maindataB-G.csv')
    Df1 = pandas.read_csv('.\data\lianhangB-GNEW(1).csv')
    Df2 = pandas.read_csv('.\data\dongfangB-GNEW(1).csv')
    x = {}
    y = {}
    z = {}
    tl = Timeline()
    tl2 = Timeline()
    tl3 = Timeline()
    listmin = [[], [], []]
    for i in range(start, end):
        x[str(i)] = Df[Df['日期'] == i]
        y[str(i)] = Df1[Df1['日期'] == i]
        z[str(i)] = Df2[Df2['日期'] == i]
    # if i==20200715:
    #    print(x.get(str(i)))
    #   print(y.get(str(i)))
    for cell in range(start, end):
        df = x.get(str(cell))
        df1 = y.get(str(cell))
        df2 = z.get(str(cell))
        list1 = []
        list2 = []
        list3 = []
        listx = [[], []]  #
        pricelist = [list(df['机票价格'].values), list(df['航班号'].values)]
        pricelist1 = [list(df1['机票价格'].values), list(df1['航班号'].values)]
        pricelist2 = [list(df2['机票价格'].values), list(df2['航班号'].values)]
        for i in range(len(pricelist1[1])):
            listx[0].append(int(pricelist1[0][i]))
        try:
            listmin[1].append(min(listx[0]))
        except BaseException:
            listmin[1].append(None)
        for i in range(len(pricelist2[1])):
            listx[1].append(int(pricelist2[0][i]))
        try:
            listmin[2].append(min(listx[1]))
        except BaseException:
            listmin[2].append(None)
        for i in range(len(pricelist[1])):
            list1.append(int(pricelist[0][i]))
            list2.append(None)
            list3.append(None)
        try:
            listmin[0].append(min(list1))
        except BaseException:
            listmin[0].append(None)
        for i in range(len(pricelist[1])):
            if pricelist[1][i] in pricelist1[1]:  # 如果携程航班里有这一班航班
                loc = pricelist1[1].index(pricelist[1][i])
                list2[i] = int(pricelist1[0][loc])
            if pricelist[1][i] in pricelist2[1]:  # 如果携程航班里有这一班航班
                loc = pricelist2[1].index(pricelist[1][i])
                list3[i] = int(pricelist2[0][loc])
        bar = (
            Bar(init_opts=opts.InitOpts(
                theme=ThemeType.DARK,
                animation_opts=opts.AnimationOpts(
                    animation_delay=500, animation_easing="cubicOut"),
                width="1800px", height='1200px',
            )
            )
                .add_xaxis(list(df['航班号'].values))
                .add_yaxis("携程", list1, category_gap="50%", markpoint_opts=opts.MarkPointOpts(), is_selected=True)
                .add_yaxis("中国联合航空", list2, category_gap="50%", markpoint_opts=opts.MarkPointOpts(), is_selected=True)
                .add_yaxis("东方航空", list3, category_gap="50%", markpoint_opts=opts.MarkPointOpts(), is_selected=True)
                .set_series_opts(markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ), markline_opts=opts.MarkLineOpts(
                data=[
                    opts.MarkLineItem(type_="min", name="最小值"),
                    opts.MarkLineItem(type_="max", name="最大值")
                ]
            ))
                .set_global_opts(
                title_opts=opts.TitleOpts("{}各航班最低票价".format(cell)),
                datazoom_opts=opts.DataZoomOpts(pos_bottom=400),
            )
        )
        tl.add(bar, "{}".format(cell))

        barx = (
            Bar(init_opts=opts.InitOpts(
                theme=ThemeType.DARK,
                animation_opts=opts.AnimationOpts(
                    animation_delay=500, animation_easing="cubicOut"),
                width="1800px", height='1200px',
            )
            )
                .add_xaxis(list(df1['航班号'].values))
                .add_yaxis("中国联合航空", listx[0], category_gap="50%", markpoint_opts=opts.MarkPointOpts(),
                           is_selected=True)
                .set_series_opts(markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ), markline_opts=opts.MarkLineOpts(
                data=[
                    opts.MarkLineItem(type_="min", name="最小值"),
                    opts.MarkLineItem(type_="max", name="最大值")
                ]
            ))
                .set_global_opts(
                title_opts=opts.TitleOpts("{}中国联合航空官网最低票价".format(cell)),
            )
        )
        tl2.add(barx, "{}".format(cell))

        bary = (
            Bar(init_opts=opts.InitOpts(
                theme=ThemeType.DARK,
                animation_opts=opts.AnimationOpts(
                    animation_delay=500, animation_easing="cubicOut"),
                width="1800px", height='1200px',
            )
            )
                .add_xaxis(list(df2['航班号'].values))
                .add_yaxis("东方航空", listx[1], category_gap="50%", markpoint_opts=opts.MarkPointOpts(), is_selected=True)
                .set_series_opts(markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ), markline_opts=opts.MarkLineOpts(
                data=[
                    opts.MarkLineItem(type_="min", name="最小值"),
                    opts.MarkLineItem(type_="max", name="最大值")
                ]
            ))
                .set_global_opts(
                title_opts=opts.TitleOpts("{}中国联合航空官网最低票价".format(cell)),
            )
        )
        tl3.add(bary, "{}".format(cell))

        table = Table()
        row = []
        headers = ['始发地', '目的地', '航空公司', '航班号', '始发机场',
                   '到达机场', '起飞时间', '到达时间', '机票价格', '数据来源', '日期']
        for index in df.index:
            row.append(list(df.loc[index].values))
        table.add(headers, row)
        show.add(table)
    axis = []
    for i in range(start, end):
        axis.append(str(i))
    line = (
        Line()
            .add_xaxis(axis)
            .add_yaxis("携程", listmin[0])
            .add_yaxis("中国联合航空", listmin[1])
            .add_yaxis("东方航空", listmin[2])
            .set_global_opts(
            title_opts=opts.TitleOpts(title="最低票价走势图"),
        )
    )
    print(listmin)

    show.add(tl)
    show.add(tl2)
    show.add(tl3)
    show.add(line)

    show.render("./html/test.html")
