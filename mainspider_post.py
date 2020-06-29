import requests
import json
import copy

def getdata(city1,city2,date):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36' ,
        "Content-Type": "application/json",  # 声明文本类型为 json 格式,
        'Cookie': '_ga=GA1.2.1422723313.1585102199; _abtest_userid=1c296dde-d639-424f-a007-cad9975fd8d5; '
                  '_gac_UA-3748357-1=1.1585220211.Cj0KCQjwpfHzBRCiARIsAHHzyZooiSyIMjmJ_FcCpRlSJuF8h1guzQ2LWkDVHs9kewmqkaawfORabUwaAtx5EALw_wcB; _RSG=Hv4Xpi9jTt51tuATq36Hm8; '
                  '_RDG=28329d014ec74124741c6df88a04cc43e6; _RGUID=5dddb49b-3384-4e51-8c11-183d1d2b8dc1; _gcl_aw=GCL.1585220214.Cj0KCQjwpfHzBRCiARIsAHHzyZooiSyIMjmJ_FcCpRlSJuF8h1guzQ2LWkDVHs9kewmqkaawfORabUwaAtx5EALw_wcB; '
                  '_gcl_dc=GCL.1585220214.Cj0KCQjwpfHzBRCiARIsAHHzyZooiSyIMjmJ_FcCpRlSJuF8h1guzQ2LWkDVHs9kewmqkaawfORabUwaAtx5EALw_wcB; MKT_CKID=1585220215050.q49s4.k99w; GUID=09031038111353360416; '
                  '_abtest_userid=19bf1f22-d393-4415-a4c6-66ef5a7a952d; _RF1=163.125.73.52; Session=smartlinkcode=U130026&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=;'
                  ' Union=AllianceID=4897&SID=130026&OUID=&createtime=1589199056&Expires=1589803855549; MKT_CKID_LMT=1589199055579; _gid=GA1.2.1657496412.1589199056; MKT_Pagesource=PC; '
                  'FD_SearchHistorty={"type":"S","data":"S%24%u5929%u6D25%28TSN%29%24TSN%242020-05-11%24%u6DF1%u5733%28SZX%29%24SZX%24%24%24"}; _gat=1; _jzqco=%7C%7C%7C%7C%7C1.1408634404.1585220215042.1589199055588.1589199119649.1589199055588.1589199119649.0.0.0.9.9; '
                  '__zpspc=9.4.1589199055.1589199119.2%232%7Cwww.baidu.com%7C%7C%7C%7C%23; _bfa=1.1585102198351.9o303i.1.1586776655945.1589199052742.5.13.214073; _bfs=1.4; _bfi=p1%3D10320673302%26p2%3D10320673302%26v1%3D13%26v2%3D12'}
    # 一个可用的cookie池，该数据来自其他项目，经验证可用
    city={'北京': 'BJS', '广州': 'CAN', '上海': 'SHA'}
    # post提交时的城市对应的值，通过网站的URL获取到的，由于数据范围太大，本项目暂定这三个城市以减小范围
    date = date[0:4] + '-' + date[4:6] + '-' + date[6:8]
    api='https://flights.ctrip.com/itinerary/api/12808/products'
    # 通过网页查看得到的接受POST请求的接口，在network-XHR-products-header下查询到的’request URL‘，同路径还查到了payload设置

    request_payload = {  # 复制浏览器内容后处理为字典
        "flightWay": "Oneway",
        "army": "false",
        "classType": "ALL",
        "hasChild": "false",
        "hasBaby": "false",
        "searchIndex": 1,
        "token": "c91cf603fd7191a9c762fcc27b4cbf29",
        "airportParams": [
            {"dcity": city.get(city1), "acity": city.get(city2), "dcityname": city1, "acityname": city2, "date": date}]
    }
    data= json.dumps(request_payload)  # 将请求数据字典处理为json
    answer= requests.post(api, data, headers= headers).text  # 发出POST请求得到回复
    dict_load = json.loads(answer)
    return dict_load


def analyse(dict_load):  # 手动分析目标位置
    check = json.dumps(dict_load, indent=1, ensure_ascii=False)  # 由于得到是json类文件难以分析,将之转化为字典再转为格式化的json方便查看
    dic = dict_load.get('data')
    for i in dic:
        print(i)  # 找到routeList键
    dic = dic.get('routeList')
    if False:
        for i in dic:
            i = json.dumps(i, indent=1, ensure_ascii=False)
            print('----------------------------------------------------------------------')
            print(i)
    if False:
        print('===============================================================================')
        print(json.dumps(dic[0], indent=1, ensure_ascii=False))  # 找到可能目标标签legs
    legs = dic[0].get('legs')
    if False:
        # for i in legs: print(json.dumps(i, indent=1, ensure_ascii=False)) # 找到可能目标flight 和 characteristic
        flight = legs[0].get('flight')
        print(json.dumps(flight, indent=1, ensure_ascii=False))  # 得到了航班的全部基础数据，但没有价格
    if True:
        for i in legs[0].get('characteristic'):
            print(i)  # 找到价格标签lowestPrice，至此找到所有需要的数据
    return 0

# 数据层次为json-data-routeList-legs-flights 以及json-data-routeList-characteristic-lowestPrices
def message(dict_load):  # 提取数据的函数
    routeList = dict_load.get('data').get('routeList')
    msg = {}
    list= []
    if routeList is None:
        print("\n------no data-------")
        return
    for route in routeList:
        if route['routeType'] == 'Flight':  # 挑选出飞机直达的航线
            legs = route.get('legs')[0]
            flight = legs.get('flight')
            msg['Airline'] = flight.get('airlineName')  # 航空公司
            msg['FlightNumber'] = flight.get('flightNumber') #  航班号
            msg['Date'] = flight.get('departureDate')[-8:-3] + "--" + flight.get('arrivalDate')[-8:-3]  # 格式化时间
            msg['PunctualityRate'] = flight.get('punctualityRate') #  准点率
            msg['Price'] = legs.get('characteristic').get('lowestPrice') #  最低价格
            list.append(copy.copy(msg))  # 将结果字典写入list,这里使用了copy.copy的浅拷贝方法
    return list

if __name__=='__main__':  #实例程序
    list=message(getdata('北京', '上海', '20200705'))
    for i in list:
        print(i.values())
  # analyse(getdata('北京', '上海', '20200701'))






