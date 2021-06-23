import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',20)# Shows all columns
pd.set_option("display.max_rows",320)
data = pd.read_csv(r"E:\4. covid_19_data.csv")
print(data)
print(data.count())
print(data.isnull().sum())
print(sns.heatmap(data.isnull()))
print(plt.show())
print(data.head(2))
print(data.groupby('Region').sum().head(20))
print(data.groupby('Region')['Confirmed'].sum().sort_values(ascending = False).head(10))
print(data.groupby('Region')['Confirmed','Recovered'].sum())
print(data.head(2))
print(data[~(data.Confirmed <10)]) #to remove the records satisfying condition
print(data)
print(data.head(20))
print(data.groupby('Region').Confirmed.sum().sort_values(ascending = False).head(20))
print(data.groupby('Region').Deaths.sum().sort_values(ascending=True).head(20))
print(data.head(2))
print(data[data.Region == 'India']) # How many Confirmed, Deaths& Recovered cases were reported from India till 29 April 2020?
print(data.sort_values(by=['Confirmed'], ascending = True).head(50))
print(data.sort_values(by = ['Recovered'], ascending=False).head(50))
