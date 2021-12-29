import pandas as pd
import sys

## Read the data into a dataframe.
WQI = pd.read_csv('Water quality in England.csv' , sep=',', encoding='latin1')
WQI.head()

# get the mean of value of ph(mg/l)
df_pH = WQI[WQI['determinand.label'] == 'pH']
a1= df_pH["determinand.notation"].mean()

# get the mean of data of visible oil or grease(pres/nf)
df_oil = WQI[WQI['determinand.label'] == 'Oil & Grs Vs']
a2 = df_oil["determinand.notation"].mean()

# get the mean of value of Ammoniacal Nitrogen
df_Ammonia = WQI[WQI['determinand.label'] == 'Ammonia(N)']
a3 = df_Ammonia["determinand.notation"].mean()

# get the mean of value of Orthophospht
df_Orthophospht = WQI[WQI['determinand.label'] == 'Orthophospht']
a4 = df_Orthophospht["determinand.notation"].mean()

# get the mean of temperature of Water
df_temp= WQI[WQI['determinand.label'] == 'Temp Water']
a5 = df_temp["determinand.notation"].mean()

# get the mean of Oxygen, Dissolved as O2
df_o2= WQI[WQI['determinand.label'] == 'Oxygen Diss']
a6 = df_o2["determinand.notation"].mean()

# get the mean of Nitrogen, Total Oxidised as N
df_N= WQI[WQI['determinand.label'] == 'N Oxidised']
a7 = df_N["determinand.notation"].mean()

data_UK = {
        'date': "2020.01-2020.08",
        'country': "UK",
        'pH': [a1],
        'Oil & Grs Vs': [a2],
        'Ammonia(N)': [a3],
        'Orthophospht': [a4],
        'Temp Water': [a5],
        'Oxygen Diss': [a6],
        'N Oxidised': [a7]}

WQINew = pd.DataFrame(data_UK, columns = ['date', 'country', 'pH', 'Oil & Grs Vs', 'Ammonia(N)', 'Orthophospht', 'Temp Water', 'Oxygen Diss', 'N Oxidised'])
WQINew

# Print and write the dataset to a file called OUTFILE.txt.
orig_stdout = sys.stdout
f = open('OUTFILE.txt', 'w')
sys.stdout = f

print(WQINew)

sys.stdout = orig_stdout
f.close()

# Create a bar graph
import numpy as np
import matplotlib.pyplot as plt

objects = ('pH', 'Oil & Grs Vs', 'Ammonia(N)','Orthophospht', 'Temp Water', 'Oxygen Diss', 'N Oxidised')
y_pos = np.arange(len(objects))
performance = [a1,a2,a3,a4,a5,a6,a7]

plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('WQI')
plt.title('WQI in UK')

plt.show()



