#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import sys

## Read the data into a dataframe.
WQI = pd.read_csv('water quality in China.xlsx' , sep=',', encoding='latin1')
WQI.head()

# get the mean of Dissolved Oxygen (mg/L)
a1 = WQI["Dissolved Oxygen (mg/L)"].mean()
a1
# get the mean of bacteria data
WQI.column.replace(<10, 5.0).mean() # returns 1.333333
a2 = WQI["E. coli (counts/100mL)"].mean()
a2
data_China = {
        'date': "2020.01-2020.08",
        'country': "China",
        'Dissolved Oxygen': [a1],
        'Bacteria': [a2]}

WQIChina = pd.DataFrame(data_China, columns = ['date', 'country', 'Dissolved Oxygen', 'Bacteria'])
WQIChina

# Print and write the dataset to a file called OUTFILE.txt.
orig_stdout = sys.stdout
f = open('OUTFILE.txt', 'w')
sys.stdout = f

print(WQINew)

sys.stdout = orig_stdout
f.close()


