#导入 requests 库
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import re
import time

# 通过 requests 库get访问https://ncov.dxy.cn/ncovh5/view/pneumonia网址，获取网页内容
htmlContent=requests.get("https://ncov.dxy.cn/ncovh5/view/pneumonia")

# 输出网页内容
# print(htmlContent.text)

##### 解析页面中的指定内容-即id为getAreaStat的标签中的全国疫情数据
#2.读取网页
soup = BeautifulSoup(htmlContent.text.encode('latin-1').decode('utf-8'),'lxml')
#3.查找script标签id为getAreaStat
tag=str(soup.find('script',id='getAreaStat'))

today_data_json=re.findall('window.getAreaStat = (.*?)}catch\(e\)',tag, re.S)

# json解析
jsonContext = json.loads(today_data_json[0])
#
# province_list=[]
# city_list=[]
# dangerAreas_list=[]
# for province_data in jsonContext:
#
#     provinceName = str(province_data['provinceName'])
#     provinceShortName = str(province_data['provinceShortName'])
#     currentConfirmedCount = int(province_data['currentConfirmedCount'])
#     confirmedCount = int(province_data['confirmedCount'])
#     suspectedCount = int(province_data['suspectedCount'])
#     curedCount = int(province_data['curedCount'])
#     deadCount = int(province_data['deadCount'])
#     comment = str(province_data['comment'])
#     locationId = int(province_data['locationId'])
#     statisticsData = str(province_data['statisticsData'])
#     highDangerCount = int(province_data['highDangerCount'])
#     midDangerCount = int(province_data['midDangerCount'])
#     detectOrgCount = int(province_data['detectOrgCount'])
#     vaccinationOrgCount = int(province_data['vaccinationOrgCount'])
#     # 先爬取各省的数据，各市和危险地区数据暂时先不使用
#     cities_json = province_data['cities']
#
#     for cities_data in cities_json:
#         cityName=cities_data['cityName']
#         city_currentConfirmedCount=cities_data['currentConfirmedCount']
#         city_confirmedCount=cities_data['confirmedCount']
#         city_suspectedCount=cities_data['suspectedCount']
#         city_curedCount=cities_data['curedCount']
#         city_deadCount=cities_data['deadCount']
#         city_highDangerCount=cities_data['highDangerCount']
#         city_midDangerCount=cities_data['midDangerCount']
#         city_locationId=cities_data['locationId']
#         city_currentConfirmedCountStr=cities_data['currentConfirmedCountStr']
#         city_list.append([provinceName, cityName,city_locationId,city_currentConfirmedCount,city_confirmedCount,city_suspectedCount,
#         city_curedCount,city_deadCount,city_highDangerCount,city_midDangerCount,city_currentConfirmedCountStr])
#
#
#
#     dangerAreas_json = province_data['dangerAreas']
#
#     for dangerAreas_data in dangerAreas_json:
#         cityName=dangerAreas_data['cityName']
#         areaName=dangerAreas_data['areaName']
#         dangerLevel=dangerAreas_data['dangerLevel']
#         dangerAreas_list.append([provinceName,cityName,areaName,dangerLevel])
#
#     province_list.append([provinceName,provinceShortName,locationId,currentConfirmedCount,confirmedCount,suspectedCount,curedCount,deadCount,comment,statisticsData,highDangerCount,midDangerCount,detectOrgCount,vaccinationOrgCount])
#
#
# today_date=time.strftime("%Y-%m-%d", time.localtime())
# data1 =['省份名称','省份短名','省份位置id','当前确诊人数','累计确诊人数','疑似病例人数','累计确诊人数治愈人数','死亡人数','备注','历史统计数据链接','高风险地区人数','中风险地区人数','检测人数','接种疫苗数量']
# frame1=pd.DataFrame(province_list,columns=data1)
# frame1.to_csv(today_date+"的中国各省疫情数据",encoding='utf-8',index=False)
#
# data2=['省份名称','城市名称','城市位置id','当前确诊人数','累计确诊人数','疑似病例人数','累计确诊人数治愈人数','死亡人数','高风险地区人数','中风险地区人数','当前确诊人数状态']
# frame2=pd.DataFrame(city_list,columns=data2)
# frame2.to_csv(today_date+"的中国各市疫情数据",encoding='utf-8',index=False)
# data3=['省份名称','城市名称','地区名','危险等级']
# frame3=pd.DataFrame(dangerAreas_list,columns=data3)
# frame3.to_csv(today_date+"的中国危险区域数据",encoding='utf-8',index=False)
#


#访问香港历史数据链接
for province_data in jsonContext:
    province = requests.get(province_data['statisticsData']).text
    data_json = json.loads(province)['data']

    list_ = []
    for data in data_json:
        confirmedCount = int(data['confirmedCount'])
        confirmedIncr = int(data['confirmedIncr'])
        curedCount = int(data['curedCount'])
        curedIncr = int(data['curedIncr'])
        currentConfirmedCount = int(data['currentConfirmedCount'])
        currentConfirmedIncr = int(data['currentConfirmedIncr'])
        dateId = int(data['dateId'])
        deadCount = int(data['deadCount'])
        deadIncr = int(data['deadIncr'])
        highDangerCount = int(data['highDangerCount'])
        midDangerCount = int(data['midDangerCount'])
        suspectedCount = int(data['suspectedCount'])
        suspectedCountIncr = int(data['suspectedCountIncr'])
        list_.append(
            [dateId, confirmedCount, confirmedIncr, curedCount, curedIncr, curedCount, currentConfirmedCount, deadCount,
             deadIncr, highDangerCount, midDangerCount, suspectedCount, suspectedCountIncr])

    data1 = ['日期', '确诊人数总数', '新增确诊人数', '治愈人数总数', '新增治愈人数', '现在确诊人数', '现在新增确诊人数', '死亡人数', '新增死亡人数','高风险地区','中风险地区','疑似人数','新增疑似人数']

    frame = pd.DataFrame(list_, columns=data1)

    result = "../result/" + str(province_data['provinceName']) + "的疫情历史数据.csv"

    frame.to_csv(result, encoding='utf-8', index=False)