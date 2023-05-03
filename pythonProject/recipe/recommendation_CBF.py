import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("csv_file/SNO_AND_ING.csv", encoding="cp949")
df.fillna("", inplace=True)
ing_list = ['감자', '계란', '고추', '당근', '대파', '마늘', '무무', '배추', '양파', '고구마', '상추', '오이', '토마토', '고춧가루', '버섯', '앞다리', '삼겹살', '갈비', '목심', '고등어', '갈치']
my_dict = {"RCP_SNO":[], "SRAP_CNT":[], "ING_INFO":[]}
m = df['SRAP_CNT'].quantile(0.9)
df = df.loc[df["SRAP_CNT"] >= m]
# print(m)

def content_based_filtering(contents):
    for i, content in enumerate(contents):
        if content == "무":
            contents[i] = "무무"
    print(contents)
    # temp_df = pd.DataFrame(data=[["0", "0", " ".join(contents)]], columns=my_dict)
    # temp_df = temp_df.append(df)
    # print(temp_df)

    counter_vector = CountVectorizer(ngram_range=(1, 1))
    c_vector_ing_info = counter_vector.fit_transform(df['ING_INFO'])
    c_vector_my_info = counter_vector.fit_transform([" ".join(ing_list), " ".join(contents)])
    print(c_vector_ing_info.shape)

    ing_info_c_sim = cosine_similarity(c_vector_my_info[1, :], c_vector_ing_info).argsort()[:, ::-1]
    sim_index = ing_info_c_sim[:, :100].reshape(-1)

    # result = append_df.iloc[sim_index].sort_values("SRAP_CNT", ascending=False)[:100]
    result = df.iloc[sim_index]
    return result


my_result = content_based_filtering(["무", "당근"])
print(my_result)
my_result.to_csv("csv_file/temp.csv", index=False, encoding='ms949')