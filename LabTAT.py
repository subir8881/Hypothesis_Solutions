#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import scipy as sp
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf


# In[8]:


CF=pd.read_csv("D:\DATA SCIENCE ASSIGNMENTS\Assignments\Assignment 3_ Hypothesis testing\DATA SET\LabTAT.csv")


# In[11]:


print (CF)


# In[12]:


CF.describe()


# In[37]:


alpha=0.05
L1=pd.DataFrame(CF['Laboratory 1'])
L2=pd.DataFrame(CF['Laboratory 2'])
L3=pd.DataFrame(CF['Laboratory 3'])
L4=pd.DataFrame(CF['Laboratory 4'])
print(L1,L2,L3,L4)


# In[38]:


tStat, pvalue = sp.stats.f_oneway(L1,L2,L3,L4)
print("P-Value:{0} T-Statistic:{1}".format(pvalue,tStat))


# In[41]:


if pvalue < 0.05:
  print('we reject null hypothesis')
else:
  print('we accept null hypothesis')


# In[ ]:




