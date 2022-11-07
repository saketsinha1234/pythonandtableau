# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 20:31:05 2022

@author: anami
"""
import pandas as pd
#file_name = pd.read_csv('file.csv') <----format of read_csv


data = pd.read_csv('transaction.csv', sep=';')
data.info()

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

data['ProfitPerTransation'] = data['SalesPerTransaction'] - data['CostPerTransaction']

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']

data['Markup'] = round(data['Markup'],2)

print(data['Day'].dtype)

day = data['Day'].astype(str)
year = data['Year'].astype(str)

print(day.dtype)
print(year.dtype)
my_date = day + '-' + data['Month'] + '-' + year


data['date'] = my_date

data.iloc[0]

data.iloc[0:3]

data.head(5)

data.iloc[-5:]

data.iloc[:,2]

data.iloc[4,2]

split_col = data['ClientKeywords'].str.split(',' , expand=True)

data['ClientAge'] = split_col[0]

data['ClientType'] = split_col[1]

data['LengthOfContract'] = split_col[2]

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')

data['LengthOfContract'] = data['LengthOfContract'].str.replace(']' , '')

data['ItemDescription'] = data['ItemDescription'].str.lower()

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

data = pd.merge(data, seasons, on = 'Month')

data = data.drop('ClientKeywords', axis=1)

data = data.drop('Day',  axis=1)

data = data.drop(['Month' , 'Year'], axis=1)

data.to_csv('ValueInc_Cleaned.csv', index = False)
