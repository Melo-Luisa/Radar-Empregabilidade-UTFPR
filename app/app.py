
import pandas as pd

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS5alLcu-PRBDOkUCAq-6UYTyB_I04abLzscaanJMAXem7zYN7YUf9sarwPXhMB9LhshaXpTBG13nJR/pub?output=csv"

df = pd.read_csv(url)

# print(df.head(30))
# print(df.describe())
# print(df.info())
# print(df.shape)
print(df.columns)

