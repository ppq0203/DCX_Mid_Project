import pandas as pd

df = pd.read_csv("../csv_file/ING_BEFORE_Finish_2.csv", encoding="cp949")

my_dict = {"RCP_SNO":[], "ING_NAME":[], "ING_AMOUNT":[], "ING_UNIT":[]}
ing_list = ['감자', '계란', '고추', '당근', '대파', '마늘', '무', '배추', '양파', '고구마', '상추', '오이', '토마토', '고춧가루', '버섯', '앞다리', '삼겹살', '갈비', '목심', '고등어', '갈치']

temp_list = []
for (_, df_row) in df.iterrows():
    for ing_name in ing_list:
        if ing_name in df_row['ING_NAME']:
            df_row['ING_NAME'] = ing_name
            if ing_name == '무':
                df_row['ING_NAME'] = "무무"
    temp_list.append([df_row["RCP_SNO"], df_row['ING_NAME'], df_row['ING_AMOUNT'], df_row['ING_UNIT']])
# for index, ing in enumerate(ingredient_set):
#     print(index, ing)
my_df = pd.DataFrame(data=temp_list, columns=my_dict)

my_df.to_csv("../../../csv_file/ING_BEFORE_Finish_3.csv", index=False, encoding="cp949")