import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read the csv file
df = pd.read_csv("data/data-processed-공시가격_㎡-v2.csv")

# draw distribution of 공시가격
sns.displot(df["공시가격_㎡"], kde=True)
plt.title("Distribution of official price per square meter")
plt.xlabel("Official price per square meter")
plt.ylabel("Frequency")
plt.savefig("data/distribution-v5.png")