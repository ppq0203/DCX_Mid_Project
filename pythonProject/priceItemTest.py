import pandas as pd

def itemPrice(name, weight):
    df_data = pd.read_csv("csv_file/price_merge.csv", encoding="ms949")
    df_price = pd.read_csv("csv_file/price_item_list.csv", encoding="ms949")
    df_price.drop(labels='Unnamed: 0', axis=1, inplace=True)
    if name == '감자':
        df_price['price'] = round(weight * df_data.loc[df_data['item_code'] == 152, 'dpr1'])
        price = df_price.loc[df_data['item_code'] == 152, 'price']

    if name == '양파':
        df_price['price'] = round(weight * df_data.loc[df_data['item_code'] == 245, 'dpr1'])
        price = df_price.loc[df_data['item_code'] == 245, 'price']

    if name == '대파':
        df_price['price'] = round(weight * df_data.loc[df_data['item_code'] == 246, 'dpr1'])
        price = df_price.loc[df_data['item_code'] == 246, 'price']

    if name == '고추':
        df_price['price'] = round(weight * df_data.loc[df_data['item_name'] == '풋고추 청양고추(100g)', 'dpr1'])
        price = df_price.loc[df_data['item_name'] == '풋고추 청양고추(100g)', 'price']

    if name == '계란':
        df_price['price'] = round(weight * df_data.loc[df_data['item_code'] == 23, 'dpr1'])
        price = df_price.loc[df_data['item_code'] == 23, 'price']

    if name == '배추':
        df_price['price'] = round(weight * df_data.loc[df_data['item_code'] == 211, 'dpr1'])
        price = df_price.loc[df_data['item_code'] == 211, 'price']

    if name == '무':
        df_price['price'] = round(weight * df_data.loc[df_data['item_code'] == 231, 'dpr1'])
        price = df_price.loc[df_data['item_code'] == 231, 'price']

    if name == '당근':
        df_price['price'] = round(weight * df_data.loc[df_data['item_code'] == 232, 'dpr1'])
        price = df_price.loc[df_data['item_code'] == 232, 'price']

    if name == '마늘':
        df_price['price'] = round(weight * df_data.loc[df_data['item_code'] == 258, 'dpr1'])
        price = df_price.loc[df_data['item_code'] == 258, 'price']

    if name == '고구마':
        df_price['price'] = round(weight * df_data.loc[df_data['item_code'] == 151, 'dpr1'])
        price = df_price.loc[df_data['item_code'] == 151, 'price']

    if name == '상추':
        df_price['price'] = round(weight * df_data.loc[df_data['item_name'] == '상추 청(100g)', 'dpr1'])
        price = df_price.loc[df_data['item_name'] == '상추 청(100g)', 'price']

    if name == '오이':
        df_price['price'] = round(weight * df_data.loc[df_data['item_name'] == '오이 다다기계통(10개)', 'dpr1'])
        price = df_price.loc[df_data['item_name'] == '오이 다다기계통(10개)', 'price']

    if name == '토마토':
        df_price['price'] = round(weight * df_data.loc[df_data['item_code'] == 225, 'dpr1'])
        price = df_price.loc[df_data['item_code'] == 225, 'price']

    if name == '고춧가루':
        df_price['price'] = round(weight * df_data.loc[df_data['item_name'] == '고춧가루 국산(1kg)', 'dpr1'])
        price = df_price.loc[df_data['item_name'] == '고춧가루 국산(1kg)', 'price']

    if name == '버섯':
        df_price['price'] = round(weight * df_data.loc[df_data['item_code'] == 317, 'dpr1'])
        price = df_price.loc[df_data['item_code'] == 317, 'price']

    if name == '앞다리':
        df_price['price'] = round(weight * df_data.loc[df_data['item_name'] == '돼지 앞다리', 'dpr1'])
        price = df_price.loc[df_data['item_name'] == '돼지 앞다리', 'price']

    if name == '삼겹살':
        df_price['price'] = round(weight * df_data.loc[df_data['item_name'] == '돼지 삼겹살', 'dpr1'])
        price = df_price.loc[df_data['item_name'] == '돼지 삼겹살', 'price']

    if name == '갈비':
        df_price['price'] = round(weight * df_data.loc[df_data['item_name'] == '돼지 갈비', 'dpr1'])
        price = df_price.loc[df_data['item_name'] == '돼지 갈비', 'price']

    if name == '목심':
        df_price['price'] = round(weight * df_data.loc[df_data['item_name'] == '돼지 목심', 'dpr1'])
        price = df_price.loc[df_data['item_name'] == '돼지 목심', 'price']

    if name == '고등어':
        df_price['price'] = round(weight * df_data.loc[df_data['item_code'] == 611, 'dpr1'])
        price = df_price.loc[df_data['item_code'] == 611, 'price']

    if name == '갈치':
        df_price['price'] = round(weight * df_data.loc[df_data['item_code'] == 613, 'dpr1'])
        price = df_price.loc[df_data['item_code'] == 613, 'price']

    # save csv
    df_price.to_csv("csv_file/price_item_list.csv", encoding="ms949")
    return price

# 무게 - 가격
name = '감자'
weight = 0.5
# name = input("재료명")
# weight = int(input("무게"))
price = itemPrice(name, weight)
print(int(price))

if price is not None:
    print(f"{name} {weight}kg : {int(price)}원")