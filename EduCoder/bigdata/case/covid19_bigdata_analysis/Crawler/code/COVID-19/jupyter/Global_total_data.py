import json
import re

import requests
from bs4 import BeautifulSoup
import pandas as pd

htmlContent=requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
soup = BeautifulSoup(htmlContent.text.encode('latin-1').decode('utf-8'),'lxml')
#3.查找script标签id为getAreaStat
tag=str(soup.find('script',id='getListByCountryTypeService2true'))

data_json=re.findall('window.getListByCountryTypeService2true = (.*?)}catch\(e\)',tag, re.S)

# json解析
jsonContext = json.loads(data_json[0])
globals_list=[]
country_list=[]
for globals_data in jsonContext:
    continents=globals_data['continents']
    provinceName=globals_data['provinceName']
    currentConfirmedCount=globals_data['currentConfirmedCount']
    confirmedCount=globals_data['confirmedCount']

    if globals_data['showRank']==True:
        confirmedCountRank=globals_data['confirmedCountRank']
        deadCountRank=globals_data['deadCountRank']
        deadRateRank = globals_data['deadRateRank']
    else:
        confirmedCountRank = ""
        deadCountRank=""
        deadRateRank=""


    curedCount=globals_data['curedCount']
    deadCount=globals_data['deadCount']
    deadRate=globals_data['deadRate']
    statisticsData=globals_data['statisticsData']
    currentConfirmedIncr=globals_data['incrVo']['currentConfirmedIncr']
    confirmedIncr=globals_data['incrVo']['confirmedIncr']
    curedIncr=globals_data['incrVo']['curedIncr']
    deadIncr=globals_data['incrVo']['deadIncr']
    globals_list.append([continents,provinceName,currentConfirmedCount,confirmedCount,confirmedCountRank,
                  curedCount,deadCount,deadCountRank,deadRate,deadRateRank,currentConfirmedIncr,confirmedIncr,curedIncr,deadIncr])

    country_data = requests.get(globals_data['statisticsData']).text
    country_json=json.loads(country_data)['data']
    for countrys in country_json:
        confirmedCount = int(countrys['confirmedCount'])
        confirmedIncr = int(countrys['confirmedIncr'])
        curedCount = int(countrys['curedCount'])
        curedIncr = int(countrys['curedIncr'])
        currentConfirmedCount = int(countrys['currentConfirmedCount'])
        currentConfirmedIncr = int(countrys['currentConfirmedIncr'])
        dateId = int(countrys['dateId'])
        deadCount = int(countrys['deadCount'])
        deadIncr = int(countrys['deadIncr'])
        highDangerCount = int(countrys['highDangerCount'])
        midDangerCount = int(countrys['midDangerCount'])
        suspectedCount = int(countrys['suspectedCount'])
        suspectedCountIncr = int(countrys['suspectedCountIncr'])
        country_list.append(
            [dateId,continents,provinceName,confirmedCount, confirmedIncr, curedCount, curedIncr, curedCount, currentConfirmedCount, deadCount,
             deadIncr, highDangerCount, midDangerCount, suspectedCount, suspectedCountIncr])


data1 = ['大洲名', '国家名', '现在确诊人数', '确诊人数总数','确诊人数数量排名', '累计确诊人数治愈人数', '死亡人数', '死亡人数数量排名', '死亡比率', '死亡比率排名',
              '较昨日确诊人数', '确诊新增', '治愈新增','死亡新增']
frame1 = pd.DataFrame(globals_list, columns=data1)
frame1.to_csv("世界疫情统计数据.csv", encoding='utf-8', index=False)



data2 = ['日期','大洲名','国家名', '确诊人数总数', '新增确诊人数', '治愈人数总数', '新增治愈人数', '现在确诊人数', '现在新增确诊人数', '死亡人数', '新增死亡人数','高风险地区','中风险地区','疑似人数','新增疑似人数']
frame2 = pd.DataFrame(country_list, columns=data2)
frame2.to_csv("各国疫情历史数据.csv", encoding='utf-8', index=False)

