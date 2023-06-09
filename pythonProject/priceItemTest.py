import pandas as pd
df_data = pd.read_csv("csv_file/price_merge.csv", encoding="ms949")
df_price = pd.read_csv("csv_file/price_item_list.csv", encoding="ms949")
df_price.drop(labels='Unnamed: 0', axis=1, inplace=True)

def itemPrice(name, weight):
    priceN = None
    if name == '감자':
        df_price.loc[df_data['item_code'] == 152, 'price'] = round(weight * df_data.loc[df_data['item_code'] == 152, 'dpr1'])
        df_price.loc[df_data['item_code'] == 152, 'weight'] = weight
        priceN = df_price.loc[df_data['item_code'] == 152, 'price']

    if name == '양파':
        df_price.loc[df_data['item_code'] == 245, 'price'] = round(weight * df_data.loc[df_data['item_code'] == 245, 'dpr1'])
        print(df_data.loc[df_data['item_code'] == 245, 'dpr1'])
        df_price.loc[df_data['item_code'] == 245, 'weight'] = weight
        priceN = df_price.loc[df_data['item_code'] == 245, 'price']

    if name == '대파':
        df_price.loc[df_data['item_code'] == 246,'price'] = round(weight * df_data.loc[df_data['item_code'] == 246, 'dpr1'])
        df_price.loc[df_data['item_code'] == 246, 'weight'] = weight
        priceN = df_price.loc[df_data['item_code'] == 246, 'price']

    if name == '고추':
        df_price.loc[df_data['item_name'] == '풋고추 청양고추(100g)','price'] = round(weight * df_data.loc[df_data['item_name'] == '풋고추 청양고추(100g)', 'dpr1'])
        df_price.loc[df_data['item_name'] == '풋고추 청양고추(100g)', 'weight'] = weight
        priceN = df_price.loc[df_data['item_name'] == '풋고추 청양고추(100g)', 'price']

    if name == '계란':
        df_price.loc[df_data['item_code'] == 23,'price'] = round(weight * df_data.loc[df_data['item_code'] == 23, 'dpr1'])
        df_price.loc[df_data['item_code'] == 23, 'weight'] = weight
        priceN = df_price.loc[df_data['item_code'] == 23, 'price']

    if name == '배추':
        df_price.loc[df_data['item_code'] == 211,'price'] = round(weight * df_data.loc[df_data['item_code'] == 211, 'dpr1'])
        df_price.loc[df_data['item_code'] == 211, 'weight'] = weight
        priceN = df_price.loc[df_data['item_code'] == 211,'price']

    if name == '무':
        df_price.loc[df_data['item_code'] == 231,'price'] = round(weight * df_data.loc[df_data['item_code'] == 231, 'dpr1'])
        df_price.loc[df_data['item_code'] == 231, 'weight'] = weight
        priceN = df_price.loc[df_data['item_code'] == 231, 'price']

    if name == '당근':
        df_price.loc[df_data['item_code'] == 232,'price'] = round(weight * df_data.loc[df_data['item_code'] == 232, 'dpr1'])
        df_price.loc[df_data['item_code'] == 232, 'weight'] = weight
        priceN = df_price.loc[df_data['item_code'] == 232, 'price']

    if name == '마늘':
        df_price.loc[df_data['item_code'] == 258,'price'] = round(weight * df_data.loc[df_data['item_code'] == 258, 'dpr1'])
        df_price.loc[df_data['item_code'] == 258, 'weight'] = weight
        priceN = df_price.loc[df_data['item_code'] == 258, 'price']

    if name == '고구마':
        df_price.loc[df_data['item_code'] == 151,'price'] = round(weight * df_data.loc[df_data['item_code'] == 151, 'dpr1'])
        df_price.loc[df_data['item_code'] == 151, 'weight'] = weight
        priceN = df_price.loc[df_data['item_code'] == 151, 'price']

    if name == '상추':
        df_price.loc[df_data['item_name'] == '상추 청(100g)','price'] = round(weight * df_data.loc[df_data['item_name'] == '상추 청(100g)', 'dpr1'])
        df_price.loc[df_data['item_name'] == '상추 청(100g)', 'weight'] = weight
        priceN = df_price.loc[df_data['item_name'] == '상추 청(100g)', 'price']

    if name == '오이':
        df_price.loc[df_data['item_name'] == '오이 다다기계통(10개)','price'] = round(weight * df_data.loc[df_data['item_name'] == '오이 다다기계통(10개)', 'dpr1'])
        df_price.loc[df_data['item_name'] == '오이 다다기계통(10개)', 'weight'] = weight
        priceN = df_price.loc[df_data['item_name'] == '오이 다다기계통(10개)', 'price']

    if name == '토마토':
        df_price.loc[df_data['item_code'] == 225,'price'] = round(weight * df_data.loc[df_data['item_code'] == 225, 'dpr1'])
        df_price.loc[df_data['item_code'] == 225, 'weight'] = weight
        priceN = df_price.loc[df_data['item_code'] == 225, 'price']

    if name == '고춧가루':
        df_price.loc[df_data['item_name'] == '고춧가루 국산(1kg)','price'] = round(weight * df_data.loc[df_data['item_name'] == '고춧가루 국산(1kg)', 'dpr1'])
        df_price.loc[df_data['item_name'] == '고춧가루 국산(1kg)', 'weight'] = weight
        priceN = df_price.loc[df_data['item_name'] == '고춧가루 국산(1kg)', 'price']

    if name == '버섯':
        df_price.loc[df_data['item_code'] == 317,'price'] = round(weight * df_data.loc[df_data['item_code'] == 317, 'dpr1'])
        df_price.loc[df_data['item_code'] == 317, 'weight'] = weight
        priceN = df_price.loc[df_data['item_code'] == 317, 'price']

    if name == '앞다리':
        df_price.loc[df_data['item_name'] == '돼지 앞다리','price'] = round(weight * df_data.loc[df_data['item_name'] == '돼지 앞다리', 'dpr1'])
        df_price.loc[df_data['item_name'] == '돼지 앞다리', 'weight'] = weight
        priceN = df_price.loc[df_data['item_name'] == '돼지 앞다리', 'price']

    if name == '삼겹살':
        df_price.loc[df_data['item_name'] == '돼지 삼겹살','price'] = round(weight * df_data.loc[df_data['item_name'] == '돼지 삼겹살', 'dpr1'])
        df_price.loc[df_data['item_name'] == '돼지 삼겹살', 'weight'] = weight
        priceN = df_price.loc[df_data['item_name'] == '돼지 삼겹살', 'price']

    if name == '갈비':
        df_price.loc[df_data['item_name'] == '돼지 갈비','price'] = round(weight * df_data.loc[df_data['item_name'] == '돼지 갈비', 'dpr1'])
        df_price.loc[df_data['item_name'] == '돼지 갈비', 'weight'] = weight
        priceN = df_price.loc[df_data['item_name'] == '돼지 갈비', 'price']

    if name == '목심':
        df_price.loc[df_data['item_name'] == '돼지 목심','price'] = round(weight * df_data.loc[df_data['item_name'] == '돼지 목심', 'dpr1'])
        df_price.loc[df_data['item_name'] == '돼지 목심', 'weight'] = weight
        priceN = df_price.loc[df_data['item_name'] == '돼지 목심', 'price']

    if name == '고등어':
        df_price.loc[df_data['item_code'] == 611,'price'] = round(weight * df_data.loc[df_data['item_code'] == 611, 'dpr1'])
        df_price.loc[df_data['item_code'] == 611, 'weight'] = weight
        priceN = df_price.loc[df_data['item_code'] == 611, 'price']

    if name == '갈치':
        df_price.loc[df_data['item_code'] == 613,'price'] = round(weight * df_data.loc[df_data['item_code'] == 613, 'dpr1'])
        df_price.loc[df_data['item_code'] == 613, 'weight'] = weight
        priceN = df_price.loc[df_data['item_code'] == 613, 'price']

    # save csv
    df_price.to_csv("csv_file/price_item_list.csv", encoding="ms949")
    return priceN

# 무게 - 가격
while True:
    name = input("재료명: ")
    weight = int(input("무게: "))
    priceN = itemPrice(name, weight)
    if priceN is not None:
        print(f"{name} {weight}g : {int(priceN)}원")
    else:
        print(f"{name}는(은) 잘못된 재료명입니다.")
        count = input("계속하시겠습니까? (Y/N)")
        if count.upper() != 'Y':
            break