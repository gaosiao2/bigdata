import pandas as pd
import requests
import datetime
import json
def get_data():
    ##网页地址
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    ##伪请求头
    header = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36"}
    ##获取网页数据
    res = requests.get(url, headers=header).json()##字符串转json格式
    dt = json.loads(res['data'])['areaTree']
    # print(dt[0].keys())##查看有哪些键
    info = []
    t_header = ['省份', '市级', '新增确诊', '现有确诊', '累计确诊', '累计死亡', '累计治愈','无症状','死亡率','治愈率']
    for provinces in dt[0]['children']:
        pro_name = provinces['name']##省份
        for citys in provinces['children']:
            city = citys['name']##市级
            newConfirm = citys['today']['confirm']##新增确诊
            nowConfirm = citys['total']['nowConfirm']##现有确诊
            confirm = citys['total']['confirm']##累计确诊
            dead = citys['total']['dead']##累计死亡
            heal = citys['total']['heal']##累计治愈
            wzz = citys['total']['wzz']##无症状
            deadRate = citys['total']['deadRate']##死亡率
            healRate = citys['total']['healRate']##治愈率
            info.append([pro_name,city,newConfirm,nowConfirm,confirm,dead,heal,wzz,deadRate,healRate])
            data = [dict(zip(t_header,j)) for j in info]##添加表头
            pd.DataFrame(data).to_csv(".\China.csv",header=True)

    """全国累计数据"""
    res2 = requests.get(url, headers=header).json()  ##字符串转字典格式
    dt2 = json.loads(res2['data'])  ##dict类型
    dt_list = []
    dt_list.append(dt2)##转换成列表
    info2 = []
    t_header2 = ["总累计确诊", "总累计治愈", "总累计死亡", "总现有确诊", "总境外输入", "总无症状感染"]
    for total in dt_list:
        confirm = total["chinaTotal"]["confirm"]  ##总累计确诊
        heal = total["chinaTotal"]["heal"]  ##总累计治愈
        dead = total["chinaTotal"]["dead"]  ##总累计死亡
        nowConfirm = total["chinaTotal"]["nowConfirm"]  ##总现有确诊
        importedCase = total["chinaTotal"]["importedCase"]  ##总境外输入
        noInfect = total["chinaTotal"]["noInfect"]  ##总无症状感染
        info2.append([confirm, heal, dead, nowConfirm, importedCase, noInfect])
        data = [dict(zip(t_header2, j)) for j in info2]##贴表头
        pd.DataFrame(data).to_csv(".\Total.csv", header=True)

if __name__ == '__main__':
    print("开始更新数据：",datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    get_data()
    print("数据更新完毕：",datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
