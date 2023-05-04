import math
import pandas as pd

file_name = "../csv_file/21type.xlsx"


def read_21type(filename):
    df = pd.read_excel(filename, engine='openpyxl')
    df['길이cm (1개 기준)'] = df['길이cm (1개 기준)'].str.extract(r'(\d+)').astype(float)
    df['무게 kg (1개 기준)'] = df['무게 kg (1개 기준)'].str.extract(r'(\d+\.\d+)').astype(float)

    type_lengths = df['길이cm (1개 기준)']
    type_weights = df['무게 kg (1개 기준)']

    result = {}
    index = 0
    for key in df['item_name']:
        result[key] = []
        result[key].append(type_lengths[index])
        result[key].append(type_weights[index])
        index += 1

    return result


# def calc_length(weight, name, data=read_21type(file_name)):
#     if name in data:
#         q = weight / data[name][1]
#         w = data[name][0] * q
#         return round(q, 1), round(w, 1)
#     else:
#         print("Type name not found")


def calc_quantity(length, name, data=read_21type(file_name)):
    if name in data:
        q = float(length) / float(data[name][0])
        return round(q, 1)
    else:
        print("Type name not found")


def calc_weight(quantity, name, data=read_21type(file_name)):
    if name in data:
        w = float(data[name][1]) * float(quantity)
        return round(w, 1)
    else:
        print("Type name not found")


def print_info(length, name, data=read_21type(file_name)):
    quantity = calc_quantity(length, name, data)
    print("{} 개수: {:.1f}".format(name, quantity))
    weight = calc_weight(quantity, name, data)
    print("{} 무게: {:.1f}".format(name, weight))


# # 사용할 엑셀 파일 이름
# filename = "../../csv_file/21type.xlsx"
# data = read_21type(filename)
# names = data.keys()
#
# name = input("재료 이름 입력 : ")
#
# if name not in names:
#     print("잘못된 재료명입니다.")
#     exit()
#
# opt = int(input("1. 길이 입력 / 2. 무게 입력 / 3. 수량 입력 : "))
#
# if opt == 1:
#     length = int(input("길이 입력 : "))
#     print_info(length, name, data)
# elif opt == 2:
#     weight = int(input("무게 입력 : "))
#     quantity, length = calc_length(weight, name, data)
#     print("{} 개수: {:.1f}".format(name, quantity))
# elif opt == 3:
#     quantity = int(input("수량 입력 : "))
#     weight = calc_weight(quantity, name, data)
#     print("{} 무게: {:.1f}".format(name, weight))