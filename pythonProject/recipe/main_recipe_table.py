import operator

import pandas as pd
import re

df = pd.read_csv("csv_file/TB_RECIPE_SEARCH-220701.csv", encoding="cp949")
df = df.dropna(axis=0, how='any', inplace=False) # 비어있는 항목이 있는 레시피 정보는 제외
# df_rep1 = df["RGTR_ID"] # 작성자 아이디만 추출
df_rep1 = df[["RCP_SNO", "CKG_NM", "CKG_KND_ACTO_NM", "CKG_INBUN_NM", "CKG_DODF_NM", "CKG_TIME_NM", "RCMM_CNT"]]
print(df.shape)
print(df_rep1.shape)
print(df.keys())
print(df_rep1.keys())

df_rep1.to_csv("csv_file/MAIN_RECIPE_TABLE.csv", index=False, encoding='ms949')