import math
import pandas as pd

def read_9type(filename):
    df = pd.read_excel(filename, engine='openpyxl')
    df['길이 (1개 기준)'] = df['길이 (1개 기준)'].str.extract(r'(\d+)').astype(float)
    df['무게 (1개 기준)'] = df['무게 (1개 기준)'].str.extract(r'(\d+\.\d+)').astype(float)

    type_lengths = df['길이 (1개 기준)']
    type_weights = df['무게 (1개 기준)']

    result = {}
    index = 0
    for key in df['재료명']:
        result[key] = []
        result[key].append(type_lengths[index])
        result[key].append(type_weights[index])
        index += 1

    return result


def read_list(filename):
    df = pd.read_excel(filename, engine='openpyxl')
    df['길이 (1개 기준)'] = df['길이 (1개 기준)'].str.extract(r'(\d+)').astype(float)
    df['무게 (1개 기준)'] = df['무게 (1개 기준)'].str.extract(r'(\d+\.\d+)').astype(float)

    type_lengths = df['길이 (1개 기준)']
    type_weights = df['무게 (1개 기준)']

    result = {}
    index = 0
    for key in df['item_name']:
        result[key] = []
        result[key].append(type_lengths[index])
        result[key].append(type_weights[index])
        index += 1

    return result


def calc_quantity(length, name, data):
    if name in data:
        q = math.ceil(length / data[name][0] * 10 / 10)
        return q
    else:
        print("Type name not found")


def calc_weight(quantity, name, data):
    if name in data:
        w = data[name][1] * quantity
        return w
    else:
        print("Type name not found")


def print_info(length, name, data):
    quantity = calc_quantity(length, name, data)
    print("{} 개수:".format(name), quantity)

    weight = calc_weight(quantity, name, data)
    print("{} 무게:".format(name), weight)


names_9type = ["감자", "계란", "고추", "당근", "대파", "마늘", "무", "배추", "양파"]
names_list = ["고구마 밤", "상추 청", "오이 다다기계통", "토마토", "고춧가루 국산", "새송이버섯", "돼지 앞다리", "돼지 삼겹살", "돼지 갈비", "돼지 목심", "고등어", "갈치"]

# 사용할 엑셀 파일 이름
filename1 = '9type.xlsx'
filename2 = 'price_item_list.xlsx'

types_9 = read_9type(filename1)
lists = read_list(filename2)

# for name in names_9type:
#     print_info(name, types_9)

# for name in names_list:
#     print_info(name, lists)

length = 12
name = input("재료 이름 입력 : ")
length = int(input("길이 입력 : "))

if name in names_9type:
    print_info(length, name, types_9)
else:
    print_info(length, name, lists)