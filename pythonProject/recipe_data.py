import operator

import pandas as pd
import re

df = pd.read_csv("csv_file/TB_RECIPE_SEARCH-220701.csv", encoding="cp949")
df = df.dropna(axis=0, how='any', inplace=False) # 비어있는 항목이 있는 레시피 정보는 제외
df_rep1 = df["RGTR_ID"] # 작성자 아이디만 추출
# df_rep1 = df["CKG_MTRL_CN"].replace(r'\([^)]*\)', ' ', regex=True)
# df_rep1 = df_rep1.replace(r'\[[^]]*\]', '|', regex=True)
# df_rep1 = df_rep1.replace(r'\|', ' ', regex=True)
# df_rep1 = df_rep1.replace(r'\?', '', regex=True)
# df_rep1 = df_rep1.replace(r'배합초\)', '', regex=True)
# df_rep1 = df_rep1.replace(r'\d\S*\s', ' ', regex=True)
# df_rep1 = df_rep1.replace(r'\d\S*$', ' ', regex=True)

ingredient_set = set(df_rep1) # 아이디목록을 set으로 저장하여 중복제거
print(df_rep1)
for i, id in enumerate(ingredient_set): # 총 몇개의 아이디가있는지 확인
    print(i, id)
res = dict.fromkeys(ingredient_set, 0) # set으로 저장되어있는 아이디 목록을 dictionary형태로 저장
for elem in df_rep1: # 아이디별 레시피수 계산
    res[elem] += 1
print(res)
sorted_d = dict( sorted(res.items(), key=operator.itemgetter(1),reverse=True)) # 아이디별 많은 레시피를 보유중인 아이디를 내림차순으로 정렬
print('Dictionary in descending order by value : ',sorted_d) #결과값 출력

# i = 0
# for df_str in df_rep1:
#     print(i, end=" :")
#     df_str = df_str.split('|')
#     i += 1
#     for elem in df_str:
#         ingredient_set.add(elem)
#         print(elem, end=", ")
#     print()
#
# # for index, ing in enumerate(ingredient_set):
# #     print(index, ing)
#
# print(df_rep1)