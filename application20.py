import pandas as pd
df = pd.read_csv('C:/Users/Donte Patton/Downloads/dataset_2191_sleep.csv')
df.head()
import warnings
warnings.filterwarnings('ignore')

print(df.shape)

df.isnull().sum().sum()

df.isnull().sum()

df.dtypes

import pandas as pd
import numpy as np

df.replace('?', np.nan, inplace=True)

df['max_life_span'] = pd.to_numeric(df['max_life_span'], errors='coerce')
df['gestation_time'] = pd.to_numeric(df['gestation_time'], errors='coerce')
df['total_sleep'] = pd.to_numeric(df['total_sleep'], errors='coerce')

print(df.info())

df.describe()

import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(df)
plt.show()

print(df["body_weight"].describe())

sns.scatterplot(data=df, x="body_weight", y="total_sleep")
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Q1 = df["body_weight"].quantile(0.25)
Q3 = df["body_weight"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"Lower bound: {lower_bound}")
print(f"Upper bound: {upper_bound}")

outliers = df[(df["body_weight"] < lower_bound) | (df["body_weight"] > upper_bound)]
print("\n Outliers:")
print(outliers)

filtered_df = df[(df["body_weight"] >= lower_bound) & (df["body_weight"] <=upperbound)]

sns.scatterplot(data=filtered_df, x="body_weight", y="total_sleep")
plt.title("Scatterplot without Outliers")
plt.xlabel("Body Weight")
plt.ylabel("Total Sleep")
plt.grid(True)
plt.show()

print(f"\nOriginal row count: {len(df)}")
print(f"Filtered row count: {len(filtered_df)}")

from sklearn.model_selection import train_test_split

X = df.drop(columns='total_sleep')
y = df['total_sleep']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_sixe=0.2, random_state=42)