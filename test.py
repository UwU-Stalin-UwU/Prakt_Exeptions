import pandas as pd

df = pd.read_csv('var4.csv')
column_list = df.columns.to_list()
print(column_list)