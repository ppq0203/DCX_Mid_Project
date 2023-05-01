import math
import pandas as pd

# 엑셀 파일에서 데이터를 읽어서 길이와 무게 정보를 추출하는 함수를 정의
def read_excel_data(filename):
    # 주어진 파일 이름으로 pandas를 사용하여 엑셀 파일을 읽고 DataFrame에 저장
    df = pd.read_excel(filename, engine='openpyxl')

    # 길이 정보를 추출하고 숫자로 변환
    df['길이 (1개 기준)'] = df['길이 (1개 기준)'].str.extract(r'(\d+)').astype(float)
    # 무게 정보를 추출하고 숫자로 변환
    df['무게 (1개 기준)'] = df['무게 (1개 기준)'].str.extract(r'(\d+\.\d+)').astype(float)

    print(df['무게 (1개 기준)'])
    # 재료명과 길이를 매핑한 딕셔너리를 생성
    type_lengths = dict(zip(df['재료명'], df['길이 (1개 기준)']))
    # 재료명과 무게를 매핑한 딕셔너리를 생성
    type_weights = dict(zip(df['재료명'], df['무게 (1개 기준)']))

    return type_lengths, type_weights

# 주어진 길이에 필요한 재료의 개수를 계산하는 함수
def get_quantity(type_name, length, type_lengths):
    if type_name in type_lengths:
        quantity = math.ceil(length / type_lengths[type_name] * 10 / 10)
        return quantity
    else:
        return "Type name not found"

# 주어진 개수에 대한 재료의 무게를 계산하는 함수를 정의
def get_weight(type_name, quantity, type_weights):
    if type_name in type_weights:
        weight = type_weights[type_name] * quantity
        return weight
    else:
        return "Type name not found"

# 사용할 엑셀 파일 이름
filename1 = '9type.xlsx'
filename2 = 'price_item_list.xlsx'

# 길이와 무게 정보를 읽음
type_lengths, type_weights = read_excel_data(filename1)

# 필요한 감자 수미의 개수를 계산
quantity = get_quantity('양파', 1000, type_lengths)
print("양파개수:", quantity,"개")

# 필요한 감자 수미의 무게를 계산
weight = get_weight('양파', quantity, type_weights)
print("양파무게:", weight,"kg")