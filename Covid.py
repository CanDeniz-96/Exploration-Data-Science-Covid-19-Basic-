#Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("owid-covid-data.csv", index_col=False)
df.head()

#Take data for 02/10 
df = df[df.date == "2022-02-10"]


#Null datas:
#Dropping columns including empty lines more than %40 of rows

for i in df.columns:
    if df[i].isnull().sum() > (df.shape[0] * 0.4):
        df.drop([i], axis=1, inplace=True)


#Explore new data
df.isnull().sum()
df.describe()
df.info
df.tail()
df.head(20)


#New dataset with required columns
columns_list = ['total_cases_per_million', 'new_cases_per_million', 'total_deaths_per_million', 'population', 'population_density']

df = df[columns_list]
df.head(20)
df.isnull().sum()

#Fill the empty columns with mean of those.
for i in columns_list:
    df[i].fillna(df[i].mean(), inplace=True)

df.isnull().sum()

#Correlation between columns
df.corr()

#Drow a heatmap from the dataset
sns.heatmap(data=df)
plt.show()
