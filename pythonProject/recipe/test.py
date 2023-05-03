import numpy as np
import pandas as pd
from konlpy.tag import Kkma, Komoran, Hannanum, Okt
import re

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

fruit_list = ['감자', '계란', '고추', '당근', '대파', '마늘', '무무', '배추', '양파', '쌀쌀', '고구마', '상추', '오이', '토마토', '고춧가루', '버섯', '앞다리', '삼겹살', '갈비', '목심', '닭닭', '고등어', '갈치']

cv = CountVectorizer(ngram_range=(1, 1))
fruit_vector = cv.fit_transform([' '.join(fruit_list), '감자 계란', '배추 양파', "쌀쌀 배추"])
print(fruit_vector.shape)
print(fruit_vector.toarray())
gerne_c_sim = cosine_similarity([[0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], fruit_vector).argsort()[:, ::-1]
print(gerne_c_sim)
sim_index = gerne_c_sim[:, :3].reshape(-1)
print(sim_index)
# sim_index = sim_index[sim_index != 1]
print(sim_index)
# result = df.iloc[sim_index].sort_values('score', ascending=False)[:]

# fruit_list = ['사과 딸기', '딸기 바나나', '바나나 딸기', '수박 수박']
#
# cv = CountVectorizer(min_df=0, ngram_range=(2, 2))
# fruit_vector = cv.fit_transform(fruit_list)
# print(fruit_vector.shape)
# print(fruit_vector.toarray())
#
# ing_list = ['감자', '계란', '고추', '당근', '대파', '마늘', '무무', '배추', '양파', '쌀쌀', '고구마', '상추', '오이', '토마토', '고춧가루', '버섯', '앞다리', '삼겹살', '갈비', '목심', '닭닭', '고등어', '갈치']
# my_dict = {"RCP_SNO":[], "ING_INFO":[]}
#
# df = pd.DataFrame(data=[[0, " "]], columns=my_dict)
# temp_df = pd.DataFrame(data=[[1, " "]], columns=my_dict)
# df.append(temp_df)
# print(df)
# print(df.append(temp_df))
# my_ing_list = [["당근", 1.1], ["무", 0.5]]
# print([x[0] for x in my_ing_list])