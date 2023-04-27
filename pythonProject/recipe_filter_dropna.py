import pandas as pd

df = pd.read_csv("csv_file/RECIPE_BEFORE_Filter_Have.csv", encoding="cp949")
df.dropna(inplace=True)

df.to_csv("csv_file/RECIPE_BEFORE_Filter_Have_drop.csv", index=False, encoding="cp949")