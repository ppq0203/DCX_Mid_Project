import pandas as pd
import glob
import os

input_file = r'C:\Users\anyware\PycharmProjects\DCX_Mid_Project\pythonProject\csv_file' # csv파일들이 있는 디렉토리 위치
output_file = r'csv_file/price_merge.csv' # 병합하고 저장하려는 파일명

allFile_list = glob.glob(os.path.join(input_file, '*_pres.csv')) # glob함수로 sales_로 시작하는 파일들을 모은다
print(allFile_list)
allData = [] # 읽어 들인 csv파일 내용을 저장할 빈 리스트를 하나 만든다
for file in allFile_list:
    df = pd.read_csv(file, encoding="ms949") # for구문으로 csv파일들을 읽어 들인다
    allData.append(df) # 빈 리스트에 읽어 들인 내용을 추가한다

dataCombine = pd.concat(allData, axis=0) # concat함수를 이용해서 리스트의 내용을 병합
# axis=0은 수직으로 병합함. axis=1은 수평. ignore_index=True는 인데스 값이 기존 순서를 무시하고 순서대로 정렬되도록 한다.
# reindexing
dataCombine.reset_index(drop=True, inplace=True)
dataCombine.drop(labels='Unnamed: 0', axis=1, inplace=True)

dataCombine.to_csv(output_file, encoding="ms949") # to_csv함수로 저장한다. 인데스를 빼려면 False로 설정(index=False,)