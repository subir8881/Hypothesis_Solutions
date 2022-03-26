#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import scipy as sp
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.proportion import proportions_ztest


# In[5]:


DF=pd.read_csv("Cutlets.csv")


# In[6]:


print (DF)


# In[20]:


UnitA=pd.DataFrame(DF['Unit A'])
UnitB=pd.DataFrame(DF['Unit B'])
print (UnitA,UnitB)


# In[24]:


tStat,pValue =sp.stats.ttest_ind(UnitA,UnitB)
print("P-Value:{0} T-Statistic:{1}".format(pValue,tStat)) 

