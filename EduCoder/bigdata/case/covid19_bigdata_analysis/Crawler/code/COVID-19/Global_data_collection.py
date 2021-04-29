#导入库
import requests
import json
import pandas as pd

get=requests.get("https://file1.dxycdn.com/2021/0425/862/9475748356761347743-135.json?t=26988637")

jsonContent = json.loads(get.text)['data']

list_ = []
for i in jsonContent:
    confirmedCount=str(i['confirmedCount'])
    confirmedIncr = str(i['confirmedIncr'])
    curedCount = str(i['curedCount'])
    curedIncr = str(i['curedIncr'])
    currentConfirmedCount = str(i['currentConfirmedCount'])
    currentConfirmedIncr = str(i['currentConfirmedIncr'])
    dateId = str(i['dateId'])
    deadCount=str(i['deadCount'])
    deadIncr=str(i['deadIncr'])
    list_.append([dateId,confirmedCount,confirmedIncr,curedCount,curedIncr,curedCount,currentConfirmedCount,deadCount,deadIncr])


data =['日期','确诊人数总数','新增确诊人数','治愈人数总数','新增治愈人数','现在确诊人数','现在新增确诊人数','死亡人数','新增死亡人数']
frame=pd.DataFrame(list_,columns=data)
frame.to_csv("test.csv",encoding='utf-8',index=False)