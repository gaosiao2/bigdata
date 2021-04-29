##导入需要的库
import pandas as pd
import requests,json


url = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=provinceCompare"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
res = requests.get(url,header).json()

dt = res['data']['provinceCompare']

list_=[]
for province_name in dt.keys():
    nowConfirm=dt[province_name]['nowConfirm']
    confirmAdd = dt[province_name]['confirmAdd']
    dead = dt[province_name]['dead']
    heal = dt[province_name]['heal']
    zero = dt[province_name]['zero']

    list_.append([province_name,nowConfirm,confirmAdd,dead,heal,zero])
print(list_)

