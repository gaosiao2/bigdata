import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

### 设置浏览器信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}

#### 爬取丁香园的数据
#1.访问丁香园网址
get=requests.get("https://ncov.dxy.cn/ncovh5/view/pneumonia",headers=headers)


##### 解析页面中的指定内容-即id为getAreaStat的标签中的全国疫情数据
#2.读取网页
soup = BeautifulSoup(get.text.encode('latin-1').decode('utf-8'),'lxml')
#3.查找script标签id为getAreaStat
tag=str(soup.find('script',id='getAreaStat'))
#### 使用正则表达式获取json格式的当天疫情数据
#4.获取疫情json数据
tag=tag.replace('<script id="getAreaStat">try { window.getAreaStat = ','').replace('}catch(e){}</script>','')
#5.json解析

jsonContext = json.loads(tag)


for a in jsonContext:
    province = requests.get(a['statisticsData'],headers=headers)
    province_data=province.text

    data_json=json.loads(province_data)['data']
    list_=[]
    for data in data_json:
        confirmedCount = int(data['confirmedCount'])
        confirmedCount = int(data['confirmedCount'])
        confirmedIncr = int(data['confirmedIncr'])
        curedCount = str(data['curedCount'])
        curedIncr = str(data['curedIncr'])
        currentConfirmedCount = str(data['currentConfirmedCount'])
        currentConfirmedIncr = str(data['currentConfirmedIncr'])
        dateId = str(data['dateId'])
        deadCount = str(data['deadCount'])
        deadIncr = str(data['deadIncr'])

        list_.append(
            [dateId, confirmedCount, confirmedIncr, curedCount, curedIncr, curedCount, currentConfirmedCount, deadCount,
             deadIncr])

    data1 = ['日期', '确诊人数总数', '新增确诊人数', '治愈人数总数', '新增治愈人数', '现在确诊人数', '现在新增确诊人数', '死亡人数', '新增死亡人数']

    frame = pd.DataFrame(list_, columns=data1)

    result = "result/" + str(a['provinceName']) + "的疫情数据.csv"

    frame.to_csv(result, encoding='utf-8', index=False)