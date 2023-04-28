import csv

import pandas as pd

df = pd.read_csv("C:/Users/anyware/Documents/카카오톡 받은 파일/RECIPE_ING_NAME_LIST2.csv", encoding="cp949")
df.dropna(inplace=True)

ingri = ["감자", "계란", "당근", "홍고추", "풋고추", "꽈리고추", "청양고추", "청고추", "오이고추", "오이 고추", "건고추", "고추가루" \
         , "고춧가루", "고추", "깐마늘", "마늘", "무", "양배추", "얼갈이배추", "얼갈이 배추", "배추", "양파", "고구마", "대파", "쪽파" \
         , "파", "생강", "닭", "소고기", "찹쌀", "쌀", "콩", "팥", "녹두", "시금치", "상추", "수박", "참외", "오이피클", "오이김치" \
         , "오이", "애호박", "쥬키니", "방울토마토", "토마토", "딸기", "열무", "미나리", "깻잎", "청피망", "피망", "파프리카", "멜론" \
         , "참깨", "땅콩", "느타리버섯", "팽이버섯", "새송이버섯", "사과", "배", "포도", "바나나", "세발나물", "멸치", "냉이나물", "돼지고기", "파스타면", "옥수수", "양지살", "쇠고기", "엑설런트 아이스크림", "견과류" \
         , "도미", "피자소스", "비엔나", "색소", "올리고당", "설탕", "파아슬리", "부추", "코코아파우더",  "대추" \
         , "우스타소스", "식빵", "올리브오일"]

temp_list = [[] for _ in range(len(ingri))]  # temp_list 초기화

for i, name in df.iterrows():
    for j, na in enumerate(ingri):
        if na in name["ING_NAME"]:
            temp_list[j].append(name["ING_NAME"])
            print(len(temp_list[j]))
            print(temp_list[j])
            break

# 각 ingri csv로 저장
for j, na in enumerate(ingri):
    item = {f"{na}": temp_list[j]}
    new = pd.DataFrame(item)
    print('new : \n',new)
    new.to_csv(f"csv_file/item_list/item_list_{na}.csv", encoding="cp949")


# # df 데이터프레임에서 na가 포함된 행 제거
# df = df[~df['ING_NAME'].str.contains(f"{na}")]
# df.to_csv("C:/Users/anyware/Documents/카카오톡 받은 파일/RECIPE_ING_NAME_LIST2.csv", encoding="cp949")


# for new in items:
#     print(new)
#
# for i, na in enumerate(ingri):
#     item[na] = temp_list[i]
#
# print(item[na])

# for i, na in enumerate(item.):
#     na.to_csv("csv_file/item_list" + ingri[i] + ".csv", encoding="cp949")


# temp_list = []
#
# for i, name in df.iterrows():
#     # print(name["ING_NAME"])
#     if '청고추' in name["ING_NAME"]:
#         temp_list.append(name["ING_NAME"])
# print(len(temp_list))
#
# item = pd.DataFrame()
# item['청고추'] = temp_list
#
# item.to_csv("csv_file/item_list.csv", index=False, encoding="cp949")

# item = pd.read_csv("csv_file/item_list.csv", encoding="cp949")
#
# for i, name in df.iterrows():
#     # print(name["ING_NAME"])
#     if '감자' in name["ING_NAME"]:
#         temp_list.append(name["ING_NAME"])
#
# for temp in temp_list:
#     print(temp)
# print(len(temp_list))
#
# item2 = pd.DataFrame({'감자': temp_list})
# new = item.append(item2)
# # item['감자'] = item['감자'].fillna()
# # item['감자'] = temp_list
# # print(df[df['ING_NAME'].str.contains('고추')])
#
# print(new)
#
# new.to_csv("csv_file/item_list.csv", index=False, encoding="cp949")
