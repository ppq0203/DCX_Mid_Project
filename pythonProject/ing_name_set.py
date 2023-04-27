import numpy as np
import pandas as pd
from konlpy.tag import Kkma, Komoran, Hannanum, Okt

df = pd.read_csv("csv_file/RECIPE_BEFORE_Filter_Have.csv", encoding="cp949")

name_set = set()

for name in df["ING_AMOUNT"]:
    name_set.add(name)

print(len(name_set))

sample = list(["가지", "감자", "계란", "고구마", "고추", "당근", "된장", "간장", "마늘", "밀가루", "배추", "생선", "식빵", "호박", "양파", "오이", "오리", "옥수수", "참치", "토마토", "대파"])

list_sample_all = []
for sam in sample:
    print(type(sam))
    for name in list(name_set):
        if type(name) != float and name.find(sam) != -1:
            list_sample_all.append(name)
            name_set.remove(name)


print(len(list_sample_all))
print(len(name_set))


df.to_csv("csv_file/RECIPE_BEFORE_Filter_Have2.csv", index=False, encoding='ms949')