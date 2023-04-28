import pandas as pd

df = pd.read_csv("csv_file/RECIPE_BEFORE_Filter_Have2.csv", encoding="cp949")
df.dropna(inplace=True)

# df.loc[:, "ING_AMOUNT"].replace(r'//.*', '', regex=True, inplace=True)
# df.loc[:, "ING_AMOUNT"].replace(r'\.\..*', '', regex=True, inplace=True)
# df.loc[:, "ING_AMOUNT"].replace(r'-', '', regex=True, inplace=True)
# df.loc[:, "ING_AMOUNT"].replace(r'.*:.*', '', regex=True, inplace=True)
# df.loc[:, "ING_AMOUNT"].replace(r'.....+', '', regex=True, inplace=True)
df.loc[:, "ING_AMOUNT"].replace(r'.*[가-힣ㄱ-ㅎㅏ-ㅣ].*', '', regex=True, inplace=True)
df.loc[:, "ING_AMOUNT"].replace(r'.*×.*', '', regex=True, inplace=True)
df.loc[:, "ING_AMOUNT"].replace(r'.*[a-zA-Z:].*', '', regex=True, inplace=True)
df.loc[:, "ING_AMOUNT"].replace(r'.*[\+\*\%\)].*', '', regex=True, inplace=True)
df.loc[:, "ING_AMOUNT"].replace(r'\./', '/', regex=True, inplace=True)
df.loc[:, "ING_AMOUNT"].replace(r'\.1/', '&1/', regex=True, inplace=True)
df.loc[:, "ING_AMOUNT"].replace(r'\.\.', '.', regex=True, inplace=True)
df.drop(df[df["ING_AMOUNT"].isin([' ', '  ', '   ', '    ', '/', '.', '·'])].index, inplace=True)

df.to_csv("csv_file/RECIPE_BEFORE_Filter_Have2_drop.csv", index=False, encoding="cp949")