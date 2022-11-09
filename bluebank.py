# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 19:02:05 2022

@author: anami
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

json_file = open('loan_data_json.json')
data = json.load(json_file)

with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    print(data)

loandata = pd.DataFrame(data)

loandata['purpose'].unique()

loandata.describe()

loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

loandata.info()
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

arr = np.array([1, 2, 3, 4])

arr = np.array(43)

arr = np.array([[1,2,3],[4,5,6]])



length = len(loandata)
ficocat = []

for x in range(0,length):
    category = loandata['fico'][x]
    if category >= 300 and category < 400:
        cat = 'Very Poor'
    elif category >= 400 and category < 600:
        cat = 'Poor'
    elif category >= 601 and category < 660:
        cat = 'Fair'
    elif category >= 660 and category < 700:
        cat = 'Good'
    elif category >= 700:
        cat = 'Excellent'
    else:
        cat = 'Unknown'
    ficocat.append(cat)

ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat


i=1
while i<10:
    print(i)
    i = i + 1


length = len(loandata)
ficocat = []

for x in range(0,length):
    category = 'red'
    
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 700:
            cat = 'Good'
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
            
    except:
        cat = 'Error - Unknown'
    ficocat.append(cat)

loandata.info()

loandata.loc[loandata['int.rate'] > 0.12,'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12,'int.rate.type'] = 'Low'

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color='green',width=0.1)
plt.show

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'red',width=0.2)
plt.show

ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color='#4caf50')
plt.show


loandata.to_csv('loan_cleaned.csv', index = True)
