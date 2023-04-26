import pandas as pd
from konlpy.tag import Kkma, Komoran, Hannanum, Okt


df = pd.read_csv("csv_file/RECIPE_BEFORE_PROCESSING.csv", encoding="cp949")
df = df.dropna(subset=['ING_NAME'], how='any', axis=0).head(30)
print(df.head(30))

i = 0
for (_, df_row) in df.iterrows():
    if i > 50:
        break
    # print(i, ": ", df_row["RCP_SNO"], type(df_row["CKG_MTRL_CN"]) )
    i += 1
    print(Kkma().pos(df_row['ING_NAME']))
    print(Komoran().pos(df_row['ING_NAME']))
    print(Hannanum().pos(df_row['ING_NAME']))
    print(Okt().pos(df_row['ING_NAME']))
    print()