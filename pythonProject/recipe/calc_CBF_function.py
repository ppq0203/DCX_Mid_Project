import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ing_list = ['감자', '계란', '고추', '당근', '대파', '마늘', '무무', '배추', '양파', '고구마', '상추', '오이', '토마토', '고춧가루', '버섯', '앞다리',
                '삼겹살', '갈비', '목심', '고등어', '갈치']

def content_based_filtering(contents, df):
    for i, content in enumerate(contents):
        if content == "무":
            contents[i] = "무무"
    print(contents)
    # my_dict = {"RCP_SNO": [], "SRAP_CNT": [], "ING_INFO": []}
    # temp_df = pd.DataFrame(data=[["0", "0", " ".join(contents)]], columns=my_dict)
    # temp_df = temp_df.append(df)
    # print(temp_df)

    counter_vector = CountVectorizer(ngram_range=(1, 1))
    c_vector_ing_info = counter_vector.fit_transform(df['ING_INFO'])
    c_vector_my_info = counter_vector.fit_transform([" ".join(ing_list), " ".join(contents)])
    print(c_vector_ing_info.shape)

    ing_info_c_sim = cosine_similarity(c_vector_my_info[1, :], c_vector_ing_info).argsort()[:, ::-1]

    # target_index = df[temp_df["RCP_SNO"] == "0"].index.values
    sim_index = ing_info_c_sim[:, :200].reshape(-1)
    # sim_index = sim_index[sim_index != target_index]

    # result = append_df.iloc[sim_index].sort_values("SRAP_CNT", ascending=False)[:100]
    result = df.iloc[sim_index]
    return result

def get_prices(result_df, my_ing):
    ing_df = pd.read_csv("csv_file/ING_BEFORE_Finish_4.csv", encoding="cp949")
    ing_df = ing_df[ing_df["RCP_SNO"].isin(result_df["RCP_SNO"].tolist())]

    temp_list = []
    for (i, df_row) in result_df.iterrows():
        already_list = []
        need_list = []
        match_point = 0
        sum_price = 0
        recipe_sno = df_row["RCP_SNO"]
        ing_datas = ing_df[ing_df["RCP_SNO"] == recipe_sno]
        my_ing_set = my_ing.copy()
        for (j, ing_row) in ing_datas.iterrows():
            point = 0
            position = -1
            for (k, ing_data) in enumerate(my_ing_set):
                if ing_data[0] in ing_row["ING_NAME"]:
                    position = k
                    break
            if position != -1:
                already_list.append([my_ing_set[position][0], my_ing_set[position][1]])
                if float(ing_row["ING_AMOUNT"]) == 0:
                    point = 1
                else:
                    point = my_ing_set[position][1]/float(ing_row["ING_AMOUNT"])
                if point >= 1:
                    point = 1
                else:
                    need_amount = float(ing_row["ING_AMOUNT"])-my_ing_set[position][1]
                    # need_price = getprice(my_ing_set[0], need_amount)
                    need_price = 1
                    need_list.append([my_ing_set[position][0],need_amount, need_price])
                    sum_price += need_price
                match_point += point
                my_ing_set.remove(my_ing_set[position])
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

        # print(recipe_sno)
        # print(i, ing_datas)

    return temp_list
# my_result = content_based_filtering(["무", "당근"])
# print(my_result)
# my_result.to_csv("csv_file/temp.csv", index=False, encoding='ms949')

def get_prices_recipes(my_ing_list):
    my_ing_names = [x[0] for x in my_ing_list]

    df = pd.read_csv("csv_file/SNO_AND_ING.csv", encoding="cp949")
    df.fillna("", inplace=True)

    my_result = content_based_filtering(my_ing_names, df)

    temp_list = get_prices(my_result, my_ing_list)
    my_dict = {"RCP_SNO": [], "ALREADY": [], "NEED": [], "POINT": [], "PRICE": []}
    my_df = pd.DataFrame(data=temp_list, columns=my_dict)
    my_df.sort_values(by=['POINT', 'PRICE'], ascending=[False, True], inplace=True)

    print(my_df)

    my_df.to_csv("csv_file/need_price.csv", index=False, encoding='ms949')
    print(my_df)

my_ing_list = [["당근", 500], ["무", 500], ["양파", 500], ["고추", 500]]
get_prices_recipes(my_ing_list)