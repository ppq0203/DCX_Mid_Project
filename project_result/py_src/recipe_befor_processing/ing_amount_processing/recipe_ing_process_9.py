import pandas as pd

ing_df = pd.read_csv("../../../csv_file/ING_BEFORE_Finish_3.csv", encoding="cp949")
ea_kg_df = pd.read_csv("csv_file/21type.csv")
name_list = list(ea_kg_df["item_name"].dropna())
weight_list = list(ea_kg_df["weight"].replace("g", '', regex=True).dropna())

print(name_list)
print(weight_list)
print(len(name_list), len(weight_list))

my_dict = {"RCP_SNO":[], "ING_NAME":[], "ING_AMOUNT":[], "ING_UNIT":[]}

temp_list = []
for (_, df_row) in ing_df.iterrows():
    temp = []
    temp.append(df_row["RCP_SNO"])
    temp.append(df_row["ING_NAME"])
    amount = float(df_row["ING_AMOUNT"])
    unit = df_row["ING_UNIT"]
    for i, elem in enumerate(name_list):
        if df_row["ING_UNIT"] == "ea" and elem in df_row["ING_NAME"]:
            amount = float(weight_list[i]) * amount
            unit = "g"
            break
    temp.append(amount)
    temp.append(unit)

    temp_list.append(temp)

# for index, ing in enumerate(ingredient_set):
#     print(index, ing)
my_df = pd.DataFrame(data=temp_list, columns=my_dict)

my_df.to_csv("../../../csv_file/ING_BEFORE_Finish_4.csv", index=False, encoding='ms949')