import pandas as pd

df = pd.read_csv('C:/Users/anyware/PycharmProjects/DCX_Mid_Project/pythonProject/csv_file/item_list/item_list_홍고추.csv', encoding="cp949")

list = ["효소", "즙"]

for na in list:
    df = df[~df['홍고추'].str.contains(f"{na}")]
    df.reset_index(drop=True, inplace=True)
    df.reset_index(drop=True, inplace=True)
    print(df)

df.drop(labels='Unnamed: 0', axis=1, inplace=True)
df.to_csv("C:/Users/anyware/PycharmProjects/DCX_Mid_Project/pythonProject/csv_file/item_final/final_홍고추.csv", encoding="cp949")