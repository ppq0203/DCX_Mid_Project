import itertools

import pandas as pd

egg1 = pd.read_csv("C:/Users/anyware/PycharmProjects/DCX_Mid_Project/pythonProject/csv_file/item_list/item_list_달걀.csv", encoding="cp949")
egg2 = pd.read_csv("C:/Users/anyware/PycharmProjects/DCX_Mid_Project/pythonProject/csv_file/item_list/item_list_계란.csv", encoding="cp949")
egg3 = pd.read_csv("C:/Users/anyware/PycharmProjects/DCX_Mid_Project/pythonProject/csv_file/item_list/item_list_흰자.csv", encoding="cp949")
egg4 = pd.read_csv("C:/Users/anyware/PycharmProjects/DCX_Mid_Project/pythonProject/csv_file/item_list/item_list_유정란.csv", encoding="cp949")
egg5 = pd.read_csv("C:/Users/anyware/PycharmProjects/DCX_Mid_Project/pythonProject/csv_file/item_list/item_list_달갈.csv", encoding="cp949")
egg6 = pd.read_csv("C:/Users/anyware/PycharmProjects/DCX_Mid_Project/pythonProject/csv_file/item_list/item_list_노른자.csv", encoding="cp949")
egg7 = pd.read_csv("C:/Users/anyware/PycharmProjects/DCX_Mid_Project/pythonProject/csv_file/item_list/item_list_초란.csv", encoding="cp949")
egg8 = pd.read_csv("C:/Users/anyware/PycharmProjects/DCX_Mid_Project/pythonProject/csv_file/item_list/item_list_왕란.csv", encoding="cp949")

# col 계란 하나로 합치기
egg1['계란'] = egg1[['달걀']].apply(lambda x: ''.join(x.astype(str)), axis=1)
egg3['계란'] = egg3[['흰자']].apply(lambda x: ''.join(x.astype(str)), axis=1)
egg4['계란'] = egg4[['유정란']].apply(lambda x: ''.join(x.astype(str)), axis=1)
egg5['계란'] = egg5[['달갈']].apply(lambda x: ''.join(x.astype(str)), axis=1)
egg6['계란'] = egg6[['노른자']].apply(lambda x: ''.join(x.astype(str)), axis=1)
egg7['계란'] = egg7[['초란']].apply(lambda x: ''.join(x.astype(str)), axis=1)
egg8['계란'] = egg8[['왕란']].apply(lambda x: ''.join(x.astype(str)), axis=1)

allData = [egg1, egg2, egg3, egg4, egg5, egg6, egg7, egg8]

# 병합
dataCombine = pd.concat(allData, axis=0)
dataCombine.reset_index(drop=True, inplace=True)
dataCombine.drop(labels='Unnamed: 0', axis=1, inplace=True)
dataCombine.drop(['달걀', '흰자', '유정란', '달갈', '노른자', '초란', '왕란'], axis=1 , inplace=True)
dataCombine.to_csv('C:/Users/anyware/PycharmProjects/DCX_Mid_Project/pythonProject/csv_file/item_list/item_new_계란.csv'
                   , encoding="cp949")

df = pd.read_csv('C:/Users/anyware/PycharmProjects/DCX_Mid_Project/pythonProject/csv_file/item_list/item_new_계란.csv'
                    , encoding="cp949")

# 계란 - list, list2, list3 제거 / 계란 흰자 - list2만/ 계란 흰자 - list3만
list = ["기름", "시금치", "동량", "달걀장", "검은깨", "삶기", "간장", "샐러드", "머랭", "소금", "과자", "국물", "장아찌" \
        , "계란국", "천일염", "고추장", "토마토", "비트", "믹스", "설탕"]

for na in list:
    df = df[~df['계란'].str.contains(f"{na}")]
    df.reset_index(drop=True, inplace=True)

df.drop(labels='Unnamed: 0', axis=1, inplace=True)
df.to_csv("C:/Users/anyware/PycharmProjects/DCX_Mid_Project/pythonProject/csv_file/item_final/final_계란.csv", encoding="cp949")