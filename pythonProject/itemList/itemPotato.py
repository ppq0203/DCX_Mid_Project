import pandas as pd

df = pd.read_csv('C:/Users/anyware/PycharmProjects/DCX_Mid_Project/pythonProject/csv_file/item_list/item_list_감자.csv', encoding="cp949")

list = ["믹스", "녹말", "녹물", "전분", "감자가루", "부침가루", "감자만두", "감자 만두", "감자가루", "돼지등뼈", "옹심이" \
        , "감자 순", "샐러드", "사라다", "감자탕", "감자 볶음", "감자튀김", "감자 튀김", "감자칩", "감자국", "스낵", "끓인물" \
        , "삶은", "삶을", "삶기", "감자면", "양념", "소금", "떡", "칼", "국물", "감자풀", "크기면", "당면", "양파", "감자라면" \
        , "수제비", "감자빵", "약", "감자 껍질", "구운감자", "과자"]

for na in list:
    df = df[~df['감자'].str.contains(f"{na}")]
    df.reset_index(drop=True, inplace=True)
    df.reset_index(drop=True, inplace=True)
    print(df)

df.drop(labels='Unnamed: 0', axis=1, inplace=True)
df.to_csv("C:/Users/anyware/PycharmProjects/DCX_Mid_Project/pythonProject/csv_file/item_final/final_감자.csv", encoding="cp949")