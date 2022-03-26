#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import scipy as sp
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn as sns
from statsmodels.stats.proportion import proportions_ztest


# In[6]:


Buyerratio=pd.read_csv("D:\DATA SCIENCE ASSIGNMENTS\Assignments\Assignment 3_ Hypothesis testing\DATA SET\BuyerRatio.csv")


# In[9]:


Buyerratio.head()


# In[10]:


Buyerratio.describe()


# In[11]:


alpha=0.05
Male = [50,142,131,70]
Female=[435,1523,1356,750]
Sales=[Male,Female]
print(Sales)


# In[16]:


chiStats = sp.stats.chi2_contingency(Sales)
print('Test t=%f p-value=%f' % (chiStats[0], chiStats[1]))
print('Interpret by p-value')


# In[14]:


if chiStats[1] < 0.05:
  print('we reject null hypothesis')
else:
  print('we accept null hypothesis')

