import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

plt.rcParams['font.family'] ='AppleGothic'
plt.rcParams['axes.unicode_minus'] =False

def plot_original_vs_log(data, city, column):
    # 원본 데이터와 로그 변환 데이터 비교 시각화
    plt.figure(figsize=(15, 6))
    
    # 원본 데이터 서브플롯
    plt.subplot(1, 2, 1)
    sns.histplot(data[column], kde=True, color='teal', edgecolor='black')
    plt.title(f"Original: {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    
    # 로그 변환 데이터 서브플롯
    plt.subplot(1, 2, 2)
    log_data = np.log(data[column])
    sns.histplot(log_data, kde=True, color='orange', edgecolor='black')
    
    plt.title(f"Log-transformed: {column}")
    plt.xlabel(f"Log({column})")
    plt.ylabel("Frequency")
    plt.legend()
    
    plt.tight_layout()
    plt.savefig("data/{}-original.png".format(city))
    # plt.show()

def plot_qq_for_column(data, city, column):
    """컬럼 데이터의 QQ 플롯 생성"""
    log_data = np.log(data[column])
    
    plt.figure(figsize=(6, 6))
    sm.qqplot(log_data, line='s', markerfacecolor='navy', markeredgecolor='none')
    plt.title(f"QQ Plot: {column}")
    plt.grid(True)
    plt.savefig("data/{}-qq.png".format(city))
    # plt.show()


df = pd.read_csv("data/data-processed-total.csv")

# # mean and std save to csv
# mean_std_df = pd.DataFrame()
# mean_std_df["전국"] = [round(df["공시가격_㎡"].mean(), -4), round(df["공시가격_㎡"].std(), -4)]
# mean_std_df["수도권"] = [round(df[(df["시도"] == "서울특별시") | (df["시도"] == "경기도") | (df["시도"] == "인천광역시")]["공시가격_㎡"].mean(), -4), round(df[(df["시도"] == "서울특별시") | (df["시도"] == "경기도") | (df["시도"] == "인천광역시")]["공시가격_㎡"].std(), -4)]
# mean_std_df["비수도권"] = [round(df[(df["시도"] != "서울특별시") & (df["시도"] != "경기도") & (df["시도"] != "인천광역시")]["공시가격_㎡"].mean(), -4), round(df[(df["시도"] != "서울특별시") & (df["시도"] != "경기도") & (df["시도"] != "인천광역시")]["공시가격_㎡"].std(), -4)]

# for city in df["시도"].unique():
#     mean_std_df[city] = [round(df[df["시도"] == city]["공시가격_㎡"].mean(), -4), round(df[df["시도"] == city]["공시가격_㎡"].std(), -4)]

# mean_std_df.to_csv("data/mean-std-original.csv", index=False)

# # log transform
# df["공시가격_㎡"] = np.log(df["공시가격_㎡"])
# log_mean_std_df = pd.DataFrame()
# log_mean_std_df["전국"] = [round(df["공시가격_㎡"].mean(), 2), round(df["공시가격_㎡"].std(), 2)]
# log_mean_std_df["수도권"] = [round(df[(df["시도"] == "서울특별시") | (df["시도"] == "경기도") | (df["시도"] == "인천광역시")]["공시가격_㎡"].mean(), 2), round(df[(df["시도"] == "서울특별시") | (df["시도"] == "경기도") | (df["시도"] == "인천광역시")]["공시가격_㎡"].std(), 2)]
# log_mean_std_df["비수도권"] = [round(df[(df["시도"] != "서울특별시") & (df["시도"] != "경기도") & (df["시도"] != "인천광역시")]["공시가격_㎡"].mean(), 2), round(df[(df["시도"] != "서울특별시") & (df["시도"] != "경기도") & (df["시도"] != "인천광역시")]["공시가격_㎡"].std(), 2)]
# for city in df["시도"].unique():
#     log_mean_std_df[city] = [round(df[df["시도"] == city]["공시가격_㎡"].mean(), 2), round(df[df["시도"] == city]["공시가격_㎡"].std(), 2)]
# log_mean_std_df.to_csv("data/mean-std-log.csv", index=False)

# for city in df["시도"].unique():
#     plot_original_vs_log(df[df["시도"] == city], city, "공시가격_㎡")
#     plot_qq_for_column(df[df["시도"] == city], city, "공시가격_㎡")

df1 = df[(df["시도"] == "서울특별시") | (df["시도"] == "경기도") | (df["시도"] == "인천광역시")]
df2 = df[(df["시도"] != "서울특별시") & (df["시도"] != "경기도") & (df["시도"] != "인천광역시")]

# match the sample size
sample_size = min(len(df1), len(df2))
df1 = df1.sample(n=sample_size)
df2 = df2.sample(n=sample_size)

# draw dist plots of original in one figure
plt.figure(figsize=(15, 6))

plt.subplot(1, 2, 1)

sns.histplot(df1["공시가격_㎡"], kde=True, color='teal', edgecolor='black', label="수도권", stat="density")
sns.histplot(df2["공시가격_㎡"], kde=True, color='orange', edgecolor='black', label="비수도권", stat="density")
plt.title("Distribution of 공시가격_㎡")
plt.xlabel("공시가격_㎡")
plt.ylabel("Density")
plt.legend()

# Normalize
plt.subplot(1, 2, 2)
sns.histplot(np.log(df1["공시가격_㎡"]), kde=True, color='teal', edgecolor='black', label="수도권", stat="density")
sns.histplot(np.log(df2["공시가격_㎡"]), kde=True, color='orange', edgecolor='black', label="비수도권", stat="density")
plt.title("Distribution of Log 공시가격_㎡")
plt.xlabel("Log 공시가격_㎡")
plt.ylabel("Density")
plt.legend()

plt.tight_layout()
# plt.savefig("data/dist-total.png")
plt.show()
