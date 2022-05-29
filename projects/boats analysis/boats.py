import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import pylab

boat = pd.read_csv('D:\MSBA\Interview\\boats\\boat_data.csv')

#sns.set(rc={'axes.facecolor':'lightblue', 'figure.facecolor':'lightblue'})
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)

boat.head()

# Think about what kinds of factors will influence the product page view?
# In practice, we may consider the price, product type, brand, condition… before the purchase.
# Check the numerical variable’s correlation
# Exploratory Data Analysis

sns.displot(boat['Number of views last 7 days'], bins=30)
plt.show()

# data cleaning
# Split the currency and amount
boat[['Currency','Amount']] = boat['Price'].str.split(" ",expand=True)
boat['Amount'] = boat['Amount'].astype(float)

# change to USD
dict = {'CHF' : 1.09, 'EUR' : 1.13, 'DKK': 0.15, 'Â£' : 1.35}
boat.replace({'Currency': dict},inplace=True)
boat['USD'] = boat['Currency'] * boat['Amount']

price_category = pd.cut(boat['USD'],bins=[0,50001,110001,290001,400001,np.inf],labels=['Under 50K','Cheap','Average','Expensive', 'Very Expensive'])
boat.insert(1,'USD Price Group',price_category)
boat['USD'].describe().apply(lambda x: format(x, 'f'))

# clarify boat type, condition of boat and engine
boat[['Boat Type - Main','Boat Type - 2nd', 'Boat Type - 3rd']] = boat['Boat Type'].str.split(",",expand=True)
boat[['Condition', 'Fuel']] = boat['Type'].str.split(",",expand=True)

# calculate age
boat['Age'] = 2022 - boat['Year Built']
boat['Age'] = boat['Age'].replace(2022, 0) # Replace 2022 with 0
# convert age to categorical group
age_category = pd.cut(boat.Age,bins=[0,6,17,28,51,101,np.inf],labels=['0-5 years', '6-16 years','17-27 years', '28-50 years', '51-100 years', '101+ years'])
boat.insert(19,'Age Group',age_category)

#split location into country, region, sub region.
boat[['Country', 'Region', 'Sub Region']] = boat['Location'].str.split('» ',expand=True)
boat['Country'] = boat['Country'].str.replace(' Â', '')
boat['Region'] = boat['Region'].str.replace(' Â', '')

pv_category = pd.cut(boat['Number of views last 7 days'],bins=[0,71,111,176,1301,3263],labels=['Low', 'Medium','More than avergae', 'Good', 'Best'])
boat.insert(22,'PV Group',pv_category)
sns.displot(boat['PV Group'])
plt.show()

boat.isnull().sum()
print(boat[boat['USD Price Group'].isnull()]['Currency'])

# we can’t find any that has a significant relationship with page view.

boat = boat.drop(['Amount','Currency','Year Built'],axis = 1)
view = boat.pop('Number of views last 7 days')
boat['# of views'] = view
plt.figure(figsize=(20, 6))
mask = np.triu(np.ones_like(boat.corr(), dtype=np.bool_))
heatmap = sns.heatmap(boat.corr(), mask=mask, vmin=-1, vmax=1, annot=True, cmap='BrBG')
heatmap.set_title('Triangle Correlation Heatmap', fontdict={'fontsize':18}, pad=16)
plt.show()

boat.to_csv('boats_new.csv')