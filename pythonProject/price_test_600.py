import pandas as pd
import requests

def code600(item_code):
    df_data = pd.read_csv("csv_file/price_" + item_code + "_v1.csv", encoding="ms949")
    df_data = df_data.copy()
    # 불필요한 col drop
    df_data.drop(labels='Unnamed: 0', axis=1, inplace=True)
    print(df_data)

    # rank data delete
    print(df_data['rank'].value_counts())
    df_data = df_data[~df_data['rank'].str.contains('중품')]
    df_data = df_data[~df_data['rank'].str.contains('小')]
    df_data = df_data[~df_data['kind_name'].str.contains('냉동')]
    # reindexing
    df_data.reset_index(drop=True, inplace=True)

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
    print(df_data.dtypes)
    df_data['dpr1'] = pd.to_numeric(df_data['dpr1'])
    df_data.drop(df_data[(df_data['dpr1'] == 0)].index, inplace=True)
    # reindexing
    df_data.reset_index(drop=True, inplace=True)

    # per 1kg
    # 고등어 1마리 400g
    df_data.loc[df_data['item_code'] == 611, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 611, 'dpr1'] * 2.5)
    # 갈치 250g
    df_data.loc[df_data['item_code'] == 613, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 613, 'dpr1'] * 4)
    # 조기 300g
    df_data.loc[df_data['item_code'] == 614, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 614, 'dpr1'] * (10 / 3))
    # 명태 580g
    df_data.loc[df_data['item_code'] == 615, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 615, 'dpr1'] * (100 / 58))
    # 물오징어 1kg 당 2.5마리
    df_data.loc[df_data['item_code'] == 619, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 619, 'dpr1'] * 2.5)
    # 건미역
    df_data.loc[df_data['item_code'] == 642, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 642, 'dpr1'] * 10)
    # 굵은소금
    df_data.loc[df_data['item_code'] == 652, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 652, 'dpr1'] / 5)
    print(df_data['dpr1'])

    # unit 1
    df_data.drop(['unit'], axis=1, inplace=True)
    df_data.insert(6, 'unit', 1)
    print(df_data['unit'])

    # drop
    df_data.drop(['kind_name'], axis=1, inplace=True)
    df_data.drop(columns=df_data.loc[:, 'day2':], inplace=True)
    print(df_data)

    df_data.to_csv("csv_file/price_" + item_code + "_pres.csv", encoding="ms949")

    # df_copy = df_data[['item_name', "item_code", "dpr1"]]
    # for df_row in df_copy:
    #     print(df_row)
    #
    # print(df_copy.shape)
