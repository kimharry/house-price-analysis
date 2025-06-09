import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

plt.rcParams['font.family'] ='AppleGothic'
plt.rcParams['axes.unicode_minus'] =False

# draw density plot of 공시가격_㎡ and log 공시가격_㎡ of all cities
# each city should be drawn in each figure and saved to a separated file
# the figure should have two subplots, one for original data, one for log data
# the plots should be compared with total data
df = pd.read_csv("data/data-processed-total.csv")
for city in df["시도"].unique():
    plt.figure(figsize=(15, 6))
    plt.subplot(1, 2, 1)
    sns.kdeplot(df[df["시도"] == city]["공시가격_㎡"], label=city)
    sns.kdeplot(df["공시가격_㎡"], label="전국")
    plt.title("Distribution of 공시가격_㎡")
    plt.xlabel("공시가격_㎡")
    plt.ylabel("Density")
    plt.legend()

    # Normalize
    plt.subplot(1, 2, 2)
    sns.kdeplot(np.log(df[df["시도"] == city]["공시가격_㎡"]), label=city)
    sns.kdeplot(np.log(df["공시가격_㎡"]), label="전국")
    plt.title("Distribution of Log 공시가격_㎡")
    plt.xlabel("Log 공시가격_㎡")
    plt.ylabel("Density")
    plt.legend()

    plt.tight_layout()
    plt.savefig("data/dist-{}.png".format(city))
    # plt.show()