import numpy as np
import pandas as pd
from konlpy.tag import Kkma, Komoran, Hannanum, Okt

df = pd.read_csv("csv_file/RECIPE_BEFORE_PROCESSING.csv", encoding="cp949")
# df.loc[:,"ING_NAME"].replace(r'\s*', np.NaN, regex=True, inplace=True)
df.drop(df[df["ING_INFO"].isin([' ', '  ', '   ', '    '])].index, inplace=True)
df.dropna(inplace=True)
print(df.head(30))

my_dict = {"RCP_SNO":[], "ING_NAME":[], "ING_AMOUNT":[], "ING_UNIT":[]}
temp_list = []

i=0
for (_, df_row) in df.iterrows():
    # if i > 1000:
    #     break
    # # print(i, ": ", df_row["RCP_SNO"], type(df_row["CKG_MTRL_CN"]) )
    i += 1
    print(i, df_row["RCP_SNO"], df_row['ING_INFO'])
    konl_kkma = Kkma().pos(df_row['ING_INFO'])
    print(konl_kkma)
    name = []
    amount = []
    temp = []
    for (str_, kind) in konl_kkma:
        if kind == "NR" or kind == "SP":
            amount += temp
            temp = []
            amount.append(str_)
        elif len(amount) == 0:
            name.append(str_)
        else:
            temp.append(str_)
    if len(amount) > 0:
        temp_list.append([df_row["RCP_SNO"], df_row['ING_INFO'].split(amount[0])[0], "".join(amount), df_row['ING_INFO'].split(amount[-1])[-1]])
    else:
        temp_list.append([df_row["RCP_SNO"], df_row['ING_INFO'], "", ""])

my_df = pd.DataFrame(data=temp_list, columns=my_dict)

my_df.to_csv("csv_file/RECIPE_BEFORE_Filter_Have2.csv", index=False, encoding='ms949')