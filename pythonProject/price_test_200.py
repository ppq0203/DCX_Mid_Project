import pandas as pd
import requests

item_code = str(200)
df_data = pd.read_csv("csv_file/price_" + item_code + "_v1.csv", encoding="ms949")
# print(df_data)
df_data = df_data.copy()
df_data.drop(labels='Unnamed: 0', axis=1, inplace=True)
print(df_data)

# rank data delete
# print(df_data['rank'].value_counts())
df_data = df_data[~df_data['rank'].str.contains('중품')]
# print(df_data)
# reindexing
df_data.reset_index(drop=True, inplace=True)


# print(df_data)
# print(df_data['rank'].value_counts())

# add column
def combine_2rd_columns(col_1, col_2):
    result = col_1
    if not pd.isna(col_2):
        result += " " + str(col_2)
    return result


df_data["item_name"] = df_data.apply(lambda x: combine_2rd_columns(x['item_name'], x['kind_name']), axis=1)
print(df_data)

# 가격 ',' 제거
df_data['dpr1'] = df_data['dpr1'].str.replace(',', '')

# str to int
df_data.drop(df_data[(df_data['dpr1'] == '-')].index, inplace=True)
df_data['dpr1'] = pd.to_numeric(df_data['dpr1'])
# print(df_data.dtypes)

# per 1kg
# 배추 1포기 3.5kg
df_data.loc[df_data['item_code'] == 211, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 211, 'dpr1'] / 3.5)
# 양배추 1포기 3.5kg
df_data.loc[df_data['item_code'] == 212, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 212, 'dpr1'] / 3.5)
# 상추
df_data.loc[df_data['item_code'] == 214, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 214, 'dpr1'] * 10)
# 수박
df_data.loc[df_data['item_code'] == 221, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 221, 'dpr1'] / 10)
# 참외 10kg 당 약 35개 (1kg 3.5개)
df_data.loc[df_data['item_code'] == 222, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 222, 'dpr1'] * 0.35)
# 오이 1개당 240g 215g 250g 평균 235g 10개 2.35kg
df_data.loc[df_data['item_code'] == 223, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 223, 'dpr1'] / 2.35)
# 애호박 1개당 438g
df_data.loc[df_data['item_code'] == 224, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 224, 'dpr1'] * (1000 / 438))
df_data.loc[df_data['item_code'] == 226, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 226, 'dpr1'] * 10)
# 무 개당 약 2kg
df_data.loc[df_data['item_code'] == 231, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 231, 'dpr1'] / 2)
df_data.loc[df_data['item_code'] == 241, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 241, 'dpr1'] * (10 / 6))
# 오이맛 고추...?
df_data.loc[df_data['item_code'] == 242, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 242, 'dpr1'] * 10)
df_data.loc[df_data['item_code'] == 243, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 243, 'dpr1'] * 10)
df_data.loc[df_data['item_code'] == 252, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 252, 'dpr1'] * 10)
df_data.loc[df_data['item_code'] == 253, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 253, 'dpr1'] * 10)
df_data.loc[df_data['item_code'] == 255, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 255, 'dpr1'] * 10)
df_data.loc[df_data['item_code'] == 256, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 256, 'dpr1'] * 5)
# 멜론 1개 1.8kg
df_data.loc[df_data['item_code'] == 257, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 257, 'dpr1'] * (10 / 18))
print(df_data['dpr1'])

# unit 1
df_data.drop(['unit'], axis=1, inplace=True)
df_data.insert(6, 'unit', 1)
print(df_data['unit'])

# drop
df_data.drop(['kind_name'], axis=1, inplace=True)
print(df_data.loc[:, 'day2':])
df_data = df_data.drop(columns=df_data.loc[:, 'day2':])
print(df_data)

df_data.to_csv("csv_file/price_"+item_code+"_pres.csv", encoding="ms949")

# df_copy = df_data[['item_name', "item_code", "dpr1"]]
# for df_row in df_copy:
#     print(df_row)
#
# print(df_copy.shape)
