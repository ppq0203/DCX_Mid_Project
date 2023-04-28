import pandas as pd
import requests

def itemName():
    df_data = pd.read_csv("csv_file/price_merge.csv", encoding="ms949")
    print(df_data)

    # 불필요한 col drop
    df_data.drop(labels='Unnamed: 0', axis=1, inplace=True)

    # drop
    df_data.drop(columns=df_data.loc[:, 'item_code':], inplace=True)
    print(df_data)

    # save csv
    df_data.to_csv("csv_file/price_item_list.csv", encoding="ms949")
