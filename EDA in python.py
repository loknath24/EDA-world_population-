#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis (World population Analysis) IN PYTHON

# # Install all the libraries Pandas, matplotlib,seaborn

# In[24]:


get_ipython().system('pip install matplotlib')


# In[46]:


from pylab import *


# In[25]:


import pandas as pd
import seaborn as sns
import matplotlib as plt


# In[26]:


import matplotlib as plt


# # Read the data from the files and get the values into a pandas dataframe

# In[3]:


df = pd.read_csv(r"C:/Users/joybose/Downloads\world_population.csv")

df


# # Format the data to remove the scientific notation

# In[4]:


pd.set_option('display.float_format',lambda x: '%.2f' %x)


# # Take a look at the information in the dataframe

# In[5]:


df.info()


# # Describe the contents inside the dataframe parameters like  count,mean,minimum,maximum

# In[6]:


df.describe()


# # Count the amount of null values in each column

# In[11]:


df.isnull().sum()


# # Identify the amount of unique values in each column

# In[13]:


df.nunique()


# # Sort the values from largest to smallest based on a column and view only the top 10

# In[16]:


df.sort_values(by="2022 Population",ascending=False).head(10)


# # View the columns with only data types as the number

# In[51]:


df.select_dtypes(include='number')


# # View the columns with only data types as Object

# In[52]:


df.select_dtypes(include='object')


# # Find the correlation between the column values

# In[17]:


df.corr()


# # Plot the correlation graph into a HeatMap

# In[27]:


sns.heatmap(df.corr(), annot=True)

plt.rcParams['figure.figsize']=(20,7)

plt.show()


# # Analyze by grouping the columns into specific category

# In[33]:


df.groupby('Continent').mean().sort_values(by='2022 Population', ascending=False)


# # Deeper look at a  specific value in a column

# In[31]:


df[df['Continent'].str.contains('Oceania')]


# In[39]:


df2=df.groupby('Continent')[df.columns[5:13]].mean().sort_values(by='2022 Population', ascending=False)

df2


# # Use transpose 

# In[40]:


df3=df2.transpose()

df3


# # Plot the initial dataframe

# In[41]:


df2.plot()


# # Plot the transpose dataframe

# In[42]:


df3.plot()


# # Plot a BoxPlot to know about the Outliers

# In[48]:


df.boxplot(figsize=(20,10))


# In[ ]:




