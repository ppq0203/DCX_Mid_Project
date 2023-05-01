import pandas as pd

temp_df = pd.read_csv("csv_file/temp.csv", encoding="cp949")
ing_df = pd.read_csv("csv_file/ING_BEFORE_Finish_3.csv", encoding="cp949")

ing_df = ing_df[ing_df["RCP_SNO"].isin(temp_df["RCP_SNO"].tolist())]

ing_list = ['감자', '계란', '고추', '당근', '대파', '마늘', '무무', '배추', '양파', '고구마', '상추', '오이', '토마토', '고춧가루', '버섯', '앞다리', '삼겹살', '갈비', '목심', '고등어', '갈치']

my_ing = [["당근", 1.1], ["무", 0.5]]

temp_list = []


for (i, df_row) in temp_df.iterrows():
    already_list = []
    need_list = []
    match_point = 0
    sum_price = 0
    recipe_sno = df_row["RCP_SNO"]
    ing_datas = ing_df[ing_df["RCP_SNO"] == recipe_sno]
    for (j, ing_row) in ing_datas.iterrows():
        my_ing_set = []
        for (k, ing_data) in enumerate(my_ing):
            if ing_data[0] in ing_row["ING_NAME"]:
                my_ing_set = ing_data
        if my_ing_set != []:
            already_list.append([my_ing_set[0], my_ing_set[1]])
            if float(ing_row["ING_AMOUNT"]) == 0:
                point = 1
            else:
                point = my_ing_set[1]/float(ing_row["ING_AMOUNT"])
            if point >= 1:
                point = 1
            else:
                need_amount = float(ing_row["ING_AMOUNT"])-my_ing_set[1]
                # need_price = getprice(my_ing_set[0], need_amount)
                need_price = 1
                need_list.append([my_ing_set[0],need_amount, need_price])
                sum_price += need_price
            match_point += point
        elif ing_row["ING_NAME"] in ing_list:
            if ing_row["ING_NAME"] == "무무":
                ing_row["ING_NAME"] = "무"
            need_amount = float(ing_row["ING_AMOUNT"])
            # need_price = getprice(ing_row["ING_NAME"], need_amount)
            need_price = 1
            need_list.append([ing_row["ING_NAME"], need_amount, need_price])
            sum_price += need_price
        else:
            need_list.append([ing_row["ING_NAME"], 0, 0])
    temp_list.append([recipe_sno, already_list, need_list, match_point, sum_price])

    print(recipe_sno)
    print(i, ing_datas)

print(temp_list)


my_dict = {"RCP_SNO":[], "ALREADY":[], "NEED":[], "POINT":[], "PRICE":[]}
my_df = pd.DataFrame(data=temp_list, columns=my_dict)

print(my_df)

my_df.to_csv("csv_file/need_price.csv", index=False, encoding='ms949')