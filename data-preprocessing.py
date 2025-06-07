import pandas as pd

# read the csv file
df = pd.read_csv("data/data-original.csv")

# remove rows except 시도, 시군구, 전용면적, 공시가격
df = df[["시도", "시군구", "전용면적", "공시가격"]]

# remove missing values
df = df.dropna()

# calculate the price per square meter
df["공시가격_㎡"] = df["공시가격"] / df["전용면적"]

# # remove outliers using IQR
# Q1 = df["공시가격_㎡"].quantile(0.25)
# Q3 = df["공시가격_㎡"].quantile(0.75)
# IQR = Q3 - Q1
# df = df[(df["공시가격_㎡"] >= Q1 - 1.5 * IQR) & (df["공시가격_㎡"] <= Q3 + 1.5 * IQR)]

# save the cleaned data
df.to_csv("data/data-processed-total.csv", index=False)