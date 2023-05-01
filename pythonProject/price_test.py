import pandas as pd
import requests
from pythonProject.price_itemName import itemName
from pythonProject.price_test_100 import code100
from pythonProject.price_test_200 import code200
from pythonProject.price_test_300 import code300
from pythonProject.price_test_400 import code400
from pythonProject.price_test_500 import code500
from pythonProject.price_test_600 import code600
from pythonProject.price_test_merge import merge
import datetime

def crawl(item_code,date):
    key = "4325ba71-b578-41fe-bd9d-e5c81afdc067"
    url_api = "http://www.kamis.or.kr/service/price/xml.do?" \
              "action=dailyPriceByCategoryList&" \
              "p_product_cls_code=01&" \
              "p_country_code=1101&" \
              "p_regday="+date+"&" \
              "p_convert_kg_yn=N&" \
              "p_item_category_code="+item_code+"&" \
              "p_cert_key="+key+"&" \
              "p_cert_id=3260&" \
              "p_returntype=json"

    resp = requests.get(url_api)
    data = resp.json()
    print(data)
    # print(data['data']['item'])
    df_data = pd.DataFrame(data['data']['item'])
    print(df_data)
    df_data.to_csv("csv_file/price_"+item_code+"_v1.csv", encoding="ms949")

# 날짜
now = datetime.datetime.now() # 오늘 날짜
print(now.year, now.month, now.day)
days_1 = datetime.timedelta(days=1) # 오늘 날짜 기준 추가 하루
beforDate = now-days_1 # 오늘 날짜 - 1일 = 어제 날짜
print(beforDate)
date = beforDate.strftime('%Y-%m-%d') # 어제 날짜 형식 : y-m-d
print(date)

# item_code 별 원본 csv
item_code = [str(100), str(200), str(300), str(400), str(500), str(600)]
print(item_code)

# item_code 별 처리
list = [code100, code200, code300, code400, code500, code600]
for item in item_code:

    crawl(item, date)

    if item == str(100):
        list[0](item)
    elif item == str(200):
        list[1](item)
    elif item == str(300):
        list[2](item)
    elif item == str(400):
        list[3](item)
    elif item == str(500):
        list[4](item)
    elif item == str(600):
        list[5](item)

# csv 병합
print(merge())

# item_name list
print(itemName())