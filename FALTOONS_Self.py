#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import scipy as sp
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.proportion import proportions_ztest
import seaborn as sns


# In[3]:


FALTOON=pd.read_csv("D:\DATA SCIENCE ASSIGNMENTS\Assignments\Assignment 3_ Hypothesis testing\DATA SET\Faltoons.csv")


# In[4]:


FALTOON.head()


# In[6]:


FALTOON.describe()


# In[14]:


Days=FALTOON['Weekdays'].value_counts()
END=FALTOON['Weekend'].value_counts()
print (Days,END)


# In[24]:


alpha=0.05
DAY = [287, 113]
END=[233, 167]
Count=[DAY,END]
print(Count)


# In[25]:


chiStats = sp.stats.chi2_contingency(Count)
print('Test t=%f p-value=%f' % (chiStats[0], chiStats[1]))
print('Interpret by p-value')


# In[26]:


if chiStats[1] < 0.05:
  print('we reject null hypothesis')
else:
  print('we accept null hypothesis')


# In[20]:


alpha= 0.05 
#we do the cross table 
tab = FALTOON.groupby(['Weekdays', 'Weekend']).size()
count = np.array([280, 520]) #How many Male and Female
nobs = np.array([400, 400]) #Total number of Male and Female are there 

stat, pval = proportions_ztest(count, nobs,alternative='two-sided') 
#Alternative The alternative hypothesis can be either two-sided or one of the one- sided tests
#smaller means that the alternative hypothesis is prop < value
#larger means prop > value.
print('{0:0.3f}'.format(pval))
# two. sided -> means checking for equal proportions of Male and Female 
# p-value < 0.05 accept alternate hypothesis i.e.
# Unequal proportions 

stat, pval = proportions_ztest(count, nobs,alternative='larger')
print('{0:0.3f}'.format(pval))
# Ha -> Proportions of Male > Proportions of Female
# Ho -> Proportions of Female > Proportions of Male
# p-value >0.05 accept null hypothesis 
# so proportion of Female > proportion of Mal

