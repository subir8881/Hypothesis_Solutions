#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import scipy as sp
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import scipy.stats as stats


# In[6]:


COF=pd.read_csv("D:\DATA SCIENCE ASSIGNMENTS\Assignments\Assignment 3_ Hypothesis testing\DATA SET\COF.csv")


# In[7]:


COF.head()


# In[8]:


COF.describe()


# In[10]:


P=COF['Phillippines'].value_counts()
Indo=COF['Indonesia'].value_counts()
Mal=COF['Malta'].value_counts()
Indi=COF['India'].value_counts()
print(P)
print(Indo)
print(Mal)
print(Indi)


# In[12]:


alpha=0.05
Free = (271, 267, 269, 280)
Defect = (29, 33, 31, 20)
All= (Free, Defect)
print (All)


# In[13]:


chiStats = sp.stats.chi2_contingency(All)
print('Test t=%f p-value=%f' % (chiStats[0], chiStats[1]))
print('Interpret by p-value')


# In[14]:


if chiStats[1] < 0.05:
  print('we reject null hyposthesis')
else: 
    print('we accept null hypothesis')

