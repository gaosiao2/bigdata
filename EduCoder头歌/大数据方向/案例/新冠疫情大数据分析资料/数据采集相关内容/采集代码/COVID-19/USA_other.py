import pandas as pd
import requests
import datetime
import json

def get_USA_data():
    ##网页地址
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign"
    ##伪请求头
    header = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36"}
    ##获取网页数据
    res = requests.get(url, headers=header).json()##字符串转字典格式
    # print(res)
    dt = json.loads(res['data'])['foreignList']
    # print(type(dt))
    # print(dt[0].keys())##查看有哪些键
    """
    北美洲 美国各州的疫情数据
    """
    info = []
    t_header = ['城市','新增确诊','未有新增确诊','累计确诊','累计死亡','累计治愈']
    for j in dt[0]['children']:##拿到美国
        city = j['name']##城市
        confirmAdd = j['confirmAdd']##新增确诊
        confirmAddCut = j['confirmAddCut']##未有新增确诊
        confirm = j['confirm']##累计确诊
        dead = j['dead']##累计死亡
        heal = j['heal']##累计治愈
        info.append([city,confirmAdd,confirmAddCut,confirm,dead,heal])
        data = [dict(zip(t_header, j)) for j in info]  ##添加表头
        pd.DataFrame(data).to_csv("D:\PyCharm\PyCharm\GProject\crawler\data\American.csv", header=True)
"""
    其他国家的疫情数据
"""
def get_foreign_data():
    ##网页地址
    url = "https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist"
    ##伪请求头
    header = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36"}
    ##发送Get请求,获取网页数据
    res = requests.get(url, headers=header).text
    dt = json.loads(res)['data']  ##字符串转字典
    # print(dt)
    info = []
    t_header = ['大洲', '国家', '新增确诊', '现有确诊', '累计确诊', '累计死亡', '累计治愈']
    for i in dt:
        continent = i['continent']  ##大洲
        country = i['name']  ##国家
        confirmAdd = i['confirmAdd']  ##新增确诊
        nowConfirm = i['nowConfirm']  ##现有确诊
        confirm = i['confirm']  ##累计确诊
        dead = i['dead']  ##累计死亡
        heal = i['heal']  ##累计治愈
        info.append([continent, country, confirmAdd, nowConfirm, confirm, dead, heal])
        data = [dict(zip(t_header, j)) for j in info]  ##添加表头
        pd.DataFrame(data).to_csv("D:\PyCharm\PyCharm\GProject\crawler\data\other_countrys.csv", header=True)
if __name__ == '__main__':
    print("开始更新数据：",datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    get_foreign_data()
    get_USA_data()
    print("数据更新完毕：",datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
