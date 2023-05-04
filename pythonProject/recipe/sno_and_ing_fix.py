import pandas as pd

df = pd.read_csv("csv_file/SNO_AND_ING.csv", encoding="cp949")
df.fillna("", inplace=True)
ing_list = ['감자', '계란', '고추', '당근', '대파', '마늘', '무무', '배추', '양파', '고구마', '상추', '오이', '토마토', '고춧가루', '버섯', '앞다리', '삼겹살', '갈비', '목심', '고등어', '갈치']
my_dict = {"RCP_SNO": [], "SRAP_CNT": [], "ING_INFO": []}
m = df['SRAP_CNT'].quantile(0.9)
df = df.loc[df["SRAP_CNT"] >= m]

df.to_csv("csv_file/SNO_AND_ING_FIX.csv", index=False, encoding='ms949')