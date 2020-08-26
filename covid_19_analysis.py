#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt 

data=pd.read_csv(r"C:\Users\vaibhav\Downloads\datasets_557629_1441596_covid_19_india.csv")
data
data2=data.iloc[1:15,0:]
data2
data2.isnull().sum()
x="ConfirmedIndianNational"
y="ConfirmedForeignNational"
plt.scatter(x,y)
data2.groupby("Date").sum()
data2.groupby("Gender").sum()
day=data2[data2['current_status'=='hospitalize'],groupby(['month','day'])['num_cases']].sum()


# In[3]:





# In[4]:





# In[11]:





# In[15]:





# In[16]:





# In[ ]:




