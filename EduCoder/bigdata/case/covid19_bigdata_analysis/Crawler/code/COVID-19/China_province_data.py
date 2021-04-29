# 导入库
import requests
import json
import pandas as pd

list_ = []
province_list=['香港','上海','云南','台湾','广东','福建','四川','陕西','海南','浙江','北京','江苏','天津','山东','山西','湖北','河南','重庆','广西','湖南','内蒙古','甘肃','贵州','黑龙江','宁夏','辽宁','安徽','河北','江西','澳门','新疆','吉林','青海','西藏']
for provinces in province_list:
    get = requests.get("https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province="+provinces)

    jsonContent = json.loads(get.text)['data']

    for i in jsonContent:
        year = str(i['year'])
        date = str(i['date'])
        country = str(i['country'])
        province = str(i['province'])
        confirm = str(i['confirm'])
        dead = str(i['dead'])
        heal = str(i['heal'])
        confirm_add = str(i['confirm_add'])
        confirm_cuts = str(i['confirm_cuts'])
        dead_cuts = str(i['dead_cuts'])
        now_confirm_cuts = str(i['now_confirm_cuts'])
        heal_cuts = str(i['heal_cuts'])
        newConfirm = str(i['newConfirm'])
        newHeal = str(i['newHeal'])
        newDead = str(i['newDead'])
        description = str(i['description']).replace("\n","")
        wzz=str(i['wzz'])
        wzz_add=str(i['wzz_add'])
        list_.append([year, date, country, province, confirm, dead, heal, confirm_add,
                      confirm_cuts, dead_cuts, now_confirm_cuts, heal_cuts, newConfirm, newHeal, newDead, description,wzz,wzz_add])
    #


data =['年份','日期','国家','省份','确诊人数','死亡人数','治愈人数','新增确诊人数','减少确诊人数',
    '减少死亡人数','减少现在确诊人数','减少治愈人数','新增确诊人数','新增治愈人数','新增死亡人数','描述','无症状','无症状增加人数']
frame=pd.DataFrame(list_,columns=data)
frame.to_csv("test2.csv",encoding='utf-8',index=False)
