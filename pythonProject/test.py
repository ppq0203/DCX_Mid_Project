import numpy as np
import pandas as pd
from konlpy.tag import Kkma, Komoran, Hannanum, Okt
import re

# df = pd.read_csv("csv_file/RECIPE_BEFORE_Filter_Have.csv", encoding="cp949")
p = re.compile('[/\d]*')
str_test = "12/3"
print(p.search(str_test).group() == str_test)