import pandas as pd

df = pd.read_csv("../../../csv_file/ING_BEFORE_Finish.csv", encoding="cp949")

my_dict = {"RCP_SNO":[], "ING_NAME":[], "ING_AMOUNT":[], "ING_UNIT":[]}

temp_list = []
for (_, df_row) in df.iterrows():
    # print(df_row["RCP_SNO"], df_row["ING_AMOUNT"])
    if '=' in df_row["ING_AMOUNT"]:
        temp = df_row["ING_AMOUNT"].split('=')
        temp2 = temp[1].split('/')
        # print(temp, temp2)
        if temp[1] == '0':
            df_row["ING_AMOUNT"] = temp[0]
        else:
            df_row["ING_AMOUNT"] = float(temp[0]) + round(float(temp2[0])/float(temp2[1]), 1)
    elif '&' in df_row["ING_AMOUNT"]:
        temp = df_row["ING_AMOUNT"].split('&')
        temp2 = temp[1].split('/')
        # print(temp, temp2)
        df_row["ING_AMOUNT"] = float(temp[0]) + round(float(temp2[0]) / float(temp2[1]), 1)
    elif '＋' in df_row["ING_AMOUNT"]:
        temp = df_row["ING_AMOUNT"].split('＋')
        temp2 = temp[1].split('/')
        # print(temp, temp2)
        df_row["ING_AMOUNT"] = float(temp[0]) + round(float(temp2[0]) / float(temp2[1]), 1)
    else:
        if '~' in df_row["ING_AMOUNT"]:
            temp = df_row["ING_AMOUNT"].split('~')
            df_row["ING_AMOUNT"] = temp[1]
        if '～' in df_row["ING_AMOUNT"]:
            temp = df_row["ING_AMOUNT"].split('～')
            df_row["ING_AMOUNT"] = temp[1]
        if '-' in df_row["ING_AMOUNT"]:
            temp = df_row["ING_AMOUNT"].split('-')
            df_row["ING_AMOUNT"] = temp[1]
        if '//' in df_row["ING_AMOUNT"]:
            temp = df_row["ING_AMOUNT"].split('//')
            # print(temp)
            df_row["ING_AMOUNT"] = round(float(temp[0]) / float(temp[1]), 1)
        elif '/' in df_row["ING_AMOUNT"]:
            temp = df_row["ING_AMOUNT"].split('/')
            # print(temp)
            if temp[0] == '':
                df_row["ING_AMOUNT"] = round(1 / float(temp[1]), 1)
            elif temp[1] == '':
                df_row["ING_AMOUNT"] = float(temp[0])
            else:
                df_row["ING_AMOUNT"] = round(float(temp[0]) / float(temp[1]), 1)
        elif '±' in df_row["ING_AMOUNT"]:
            temp = df_row["ING_AMOUNT"].split('±')
            # print(temp)
            df_row["ING_AMOUNT"] = float(temp[0]) + float(temp[1])
        elif 'ㆍ' in df_row["ING_AMOUNT"]:
            temp = df_row["ING_AMOUNT"].split('ㆍ')
            # print(temp)
            df_row["ING_AMOUNT"] = float(temp[0]) + round(float(temp[1])/10, 1)

    if df_row["ING_UNIT"] == "bol":
        amount = round(float(df_row["ING_AMOUNT"]) * 550, 1)
        unit = 'g'
    elif df_row["ING_UNIT"] == "can":
        amount = round(float(df_row["ING_AMOUNT"]) * 200, 1)
        unit = 'g'
    elif df_row["ING_UNIT"] == "cup":
        amount = round(float(df_row["ING_AMOUNT"]) * 200, 1)
        unit = 'g'
    elif df_row["ING_UNIT"] == "korea_gram":
        amount = round(float(df_row["ING_AMOUNT"]) * 600, 1)
        unit = 'g'
    elif df_row["ING_UNIT"] == "oz":
        amount = round(float(df_row["ING_AMOUNT"]) * 28, 1)
        unit = 'g'
    elif df_row["ING_UNIT"] == "soju":
        amount = round(float(df_row["ING_AMOUNT"]) * 50, 1)
        unit = 'g'
    elif df_row["ING_UNIT"] == "spoon":
        amount = round(float(df_row["ING_AMOUNT"]) * 15, 1)
        unit = 'g'
    elif df_row["ING_UNIT"] == "t":
        amount = round(float(df_row["ING_AMOUNT"]) * 15, 1)
        unit = 'g'
    elif df_row["ING_UNIT"] == "g":
        amount = round(float(df_row["ING_AMOUNT"]), 1)
        unit = 'g'
    elif df_row["ING_UNIT"] == "ｇ":
        amount = round(float(df_row["ING_AMOUNT"]), 1)
        unit = 'g'
    elif df_row["ING_UNIT"] == "kg":
        amount = round(float(df_row["ING_AMOUNT"]) * 1000, 1)
        unit = 'g'
    elif df_row["ING_UNIT"] == "㎏":
        amount = round(float(df_row["ING_AMOUNT"]) * 1000, 1)
        unit = 'g'
    elif df_row["ING_UNIT"] == "mg":
        amount = round(float(df_row["ING_AMOUNT"])/1000, 1)
        unit = 'g'
    elif df_row["ING_UNIT"] == "mI":
        amount = round(float(df_row["ING_AMOUNT"]), 1)
        unit = 'ml'
    elif df_row["ING_UNIT"] == "ml":
        amount = round(float(df_row["ING_AMOUNT"]), 1)
        unit = 'ml'
    elif df_row["ING_UNIT"] == "mm":
        amount = round(float(df_row["ING_AMOUNT"])/10, 1)
        unit = 'cm'
    elif df_row["ING_UNIT"] == "pinch":
        amount = 0
        unit = 'g'
    else:
        amount = df_row["ING_AMOUNT"]
        unit = df_row["ING_UNIT"]
    if unit != 'cm' and unit != 'ea':
        if float(df_row["ING_AMOUNT"]) > 10000:
            amount = ""
            unit = ""
    temp_list.append([df_row["RCP_SNO"], df_row['ING_NAME'], amount, unit])
# for index, ing in enumerate(ingredient_set):
#     print(index, ing)
my_df = pd.DataFrame(data=temp_list, columns=my_dict)

my_df.drop(my_df[my_df["ING_UNIT"].isin(['', ' '])].index, inplace=True)

my_df.to_csv("../csv_file/ING_BEFORE_Finish_2.csv", index=False, encoding="cp949")