import pandas as pd
import requests

def code400(item_code):
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
    # 사과 10kg 28개 1kg 당 2.8개
    df_data.loc[df_data['item_code'] == 411, 'dpr1'] = round((df_data.loc[df_data['item_code'] == 411, 'dpr1'] * 0.28) / 1000, 1)
    # 배 15kg 23개 1kg 당 23/15개
    df_data.loc[df_data['item_code'] == 412, 'dpr1'] = round((df_data.loc[df_data['item_code'] == 412, 'dpr1'] * (10 * (23 / 150))) / 1000, 1)
    df_data.loc[df_data['item_code'] == 414, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 414, 'dpr1'] / 1000, 1)
    df_data.loc[df_data['item_code'] == 418, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 418, 'dpr1'] / 100, 1)
    # 참다래 10kg 100개, 1kg 10개
    df_data.loc[df_data['item_code'] == 419, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 419, 'dpr1'] / 1000, 1)
    # 파인애플 1개 2kg
    df_data.loc[df_data['item_code'] == 420, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 420, 'dpr1'] / 2000, 1)
    # 오렌지 10개 18kg 72개, 1kg 4개
    df_data.loc[df_data['item_code'] == 421, 'dpr1'] = round((df_data.loc[df_data['item_code'] == 421, 'dpr1'] * (2 / 5)) / 1000, 1)
    # 레몬 10개 1개 155g, 10개 1.6kg
    df_data.loc[df_data['item_code'] == 424, 'dpr1'] = round((df_data.loc[df_data['item_code'] == 424, 'dpr1'] / 1.6) / 1000, 1)
    # 망고 1개 375g
    df_data.loc[df_data['item_code'] == 428, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 428, 'dpr1'] / 375, 1)
    # 아보카도 200g
    df_data.loc[df_data['item_code'] == 430, 'dpr1'] = round(df_data.loc[df_data['item_code'] == 430, 'dpr1'] / 200, 1)
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
