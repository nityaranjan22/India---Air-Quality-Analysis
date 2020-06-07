#%%
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#%%

df = pd.read_csv("dataset.csv")

#%%

#print(df.describe())
#print(df.columns)

#%%
replacements = {'state': {r'Uttaranchal': 'Uttarakhand', }}
df.replace(replacements, regex = True, inplace = True)
#%%
df.dropna(axis = 0, subset = ['type'])
df = df.dropna(axis = 0, subset = ['location'])
df = df.dropna(axis = 0, subset = ['so2'])
#%%
df.drop_duplicates()

df.isnull().sum()
#%%
df.drop(['stn_code'], inplace = True, axis = 1)
df.drop(['agency'], inplace = True,axis = 1)
df.drop(['location_monitoring_station'], inplace = True, axis = 1)
df.drop(['sampling_date'], inplace = True,axis = 1)
#%%
#print(df.head)
#df.to_csv("clean.csv")

#print(df['type'].value_counts())

#cities_ap = df['location'][df['state']=='Andhra Pradesh']
#print(cities_ap.value_counts())
#%%
sns.catplot(x = "type", kind = "count", palette = "ch: 0.25", data = df)
#%%
#bar plot of so2 vs state - desc order
df[['so2', 'state']].groupby(['state']).median().sort_values("so2", ascending = False).plot.bar()
#%%
# bar plot of no2 vs state - desc order
df[['no2', 'state']].groupby(['state']).median().sort_values("no2", ascending = False).plot.bar(color = 'r')
#%%
# rspm = PM10
df[['rspm', 'state']].groupby(['state']).median().sort_values("rspm", ascending = False).plot.bar(color = 'r')
#%%
# spm
df[['spm', 'state']].groupby(['state']).median().sort_values("spm", ascending = False).plot.bar(color = 'r')
#%%
# pm2_5
df[['pm2_5', 'state']].groupby(['state']).median().sort_values("pm2_5", ascending = False).plot.bar(color = 'r')
#%%
plt.show()
#%%
#Scatter plots of all columns
sns.set()
cols = ['so2', 'no2', 'rspm', 'spm', 'pm2_5']
sns.pairplot(df[cols], size = 2.5)
plt.show()
#%%
#taking only Delhi data
df_delhi = df[df['location'] == 'Delhi']
#%%
# showing the relationship between no2 vs rspm (hardly increasing correlation)
sns.regplot(x = 'no2', y = 'rspm', data = df_delhi)
plt.ylim(0,)
plt.show()
#%%
#Relationship between no2 vs so2 (increasing correlation)
sns.regplot(x = 'no2', y = 'so2',data = df_delhi)
plt.ylim(0,)
plt.show()
#%%
#Relationship between so2 vs rspm (hardly increasing correlation)
sns.regplot(x = 'so2', y = 'rspm',data = df_delhi)
plt.ylim(0,)
plt.show()
#%%

#Correlation matrix
corrmat = df.corr()
f, ax = plt.subplots(figsize = (15, 10))
sns.heatmap(corrmat, vmax = 1, square = True, annot = True)
#%%
# Creating an year column
df['date'] = pd.to_datetime(df['date'], format = '%m/%d/%Y')
df['year'] = df['date'].dt.year # year
df['year'] = df['year'].fillna(0.0).astype(int)
df = df[(df['year']>0)]
#%%
# Heatmap Pivot with State as Row, Year as Col, No2 as Value
f, ax = plt.subplots(figsize = (10,10))
ax.set_title('{} by state and year'.format('so2'))
sns.heatmap(df.pivot_table('so2', index = 'state',
                columns = ['year'], aggfunc = 'median', margins=True),
                annot = True, cmap = 'YlGnBu', linewidths = 1, ax = ax, cbar_kws = {'label': 'Average taken Annually'})
#%%
    
    
# Heatmap Pivot with State as Row, Year as Col, So2 as Value
f, ax = plt.subplots(figsize=(10,10))
ax.set_title('{} by state and year'.format('no2'))
sns.heatmap(df.pivot_table('no2', index='state',
                columns=['year'],aggfunc='median',margins=True),
                annot = True, cmap = "YlGnBu", linewidths = 1, ax = ax,cbar_kws = {'label': 'Annual Average'})

#%%
# heatmap of rspm
f, ax = plt.subplots(figsize = (10,10))
ax.set_title('{} by state and year'.format('rspm'))
sns.heatmap(df.pivot_table('rspm', index='state',
                columns = ['year'], aggfunc = 'median', margins = True),
                annot = True, cmap = "YlGnBu", linewidths = 1, ax = ax, cbar_kws = {'label': 'Annual Average'})
#%%
# heatmap of spm
f, ax = plt.subplots(figsize = (10, 10))
ax.set_title('{} by state and year'.format('spm'))
sns.heatmap(df.pivot_table('spm', index ='state',
                columns = ['year'], aggfunc = 'median', margins = True)
                , cmap = "YlGnBu", linewidths = 0.5, ax = ax, cbar_kws = {'label': 'Annual Average'})
#%%
plt.show()

# %%
