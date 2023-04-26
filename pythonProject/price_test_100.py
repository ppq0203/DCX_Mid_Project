import pandas as pd
import requests

df_data = pd.read_csv("csv_file/price_100_v1.csv", encoding="ms949")
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

# unit data 1kg
df_data['unit'] = df_data['unit'].str.replace('kg', '')
df_data['unit'] = df_data['unit'].str.replace('g', '')
# print(df_data['unit'])

df_data['dpr1'] = df_data['dpr1'].str.replace(',', '')
# print(df_data['dpr1'])

# str to int
# print(df_data.dtypes)
df_data['dpr1'] = pd.to_numeric(df_data['dpr1'])
# print(df_data.dtypes)

# per 1kg
df_data.loc[df_data['item_code'] == 111, 'dpr1'] = df_data.loc[df_data['item_code'] == 111, 'dpr1'] / 20
df_data.loc[df_data['item_code'] == 112, 'dpr1'] = df_data.loc[df_data['item_code'] == 112, 'dpr1']
df_data.loc[df_data['item_code'] == 141, 'dpr1'] = df_data.loc[df_data['item_code'] == 141, 'dpr1'] * 2
df_data.loc[df_data['item_code'] == 142, 'dpr1'] = df_data.loc[df_data['item_code'] == 142, 'dpr1'] * 2
df_data.loc[df_data['item_code'] == 143, 'dpr1'] = df_data.loc[df_data['item_code'] == 143, 'dpr1'] * 2
df_data.loc[df_data['item_code'] == 151, 'dpr1'] = df_data.loc[df_data['item_code'] == 151, 'dpr1']
df_data.loc[df_data['item_code'] == 152, 'dpr1'] = df_data.loc[df_data['item_code'] == 152, 'dpr1'] * 10
print(df_data['dpr1'])

# unit 1
df_data.drop(['unit'], axis=1, inplace= True)
df_data.insert(6, 'unit', 1)
print(df_data['unit'])

# drop
df_data.drop(['kind_name'], axis=1, inplace=True)
print(df_data.loc[:, 'day2':])
df_data = df_data.drop(columns=df_data.loc[:, 'day2':])
print(df_data)

df_data.to_csv("csv_file/price_100_pres.csv", encoding="ms949")

# df_copy = df_data[['item_name', "item_code", "dpr1"]]
# for df_row in df_copy:
#     print(df_row)
#
# print(df_copy.shape)
