import pandas as pd
import requests

item_code = str(100)
key = "4325ba71-b578-41fe-bd9d-e5c81afdc067"
url_api = "http://www.kamis.or.kr/service/price/xml.do?" \
          "action=dailyPriceByCategoryList&" \
          "p_product_cls_code=01&" \
          "p_country_code=1101&" \
          "p_regday=2023-04-24&" \
          "p_convert_kg_yn=N&" \
          "p_item_category_code="+item_code+"&" \
          "p_cert_key="+key+"&" \
          "p_cert_id=3260&" \
          "p_returntype=json"

resp = requests.get(url_api)
data = resp.json()
print(data)
print(data['data']['item'])
df_data = pd.DataFrame(data['data']['item'])
print(df_data)
df_data.to_csv("csv_file/price_"+item_code+"_v1.csv", encoding="ms949")
