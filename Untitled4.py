#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np


# In[4]:


print(pd.__version__)


# # Series create manipulate querry delete

# In[5]:


# creating a series from list
arr = [0,1,2,3,4]
s1 = pd.Series(arr)
s1


# In[10]:


import numpy as np
n=np.random.randn(5)
index = ['a','b','c','d','e']
s2 = pd.Series(n, index=index)
s2


# In[11]:


d = {'a':1,'b':2,'c':3,'d':4,'e':5}
s3 = pd.Series(d)
s3


# # Create Dataframe
# 

# In[21]:


dates=pd.date_range('today',periods=6) #define time sequqnce index
num_arr =np.random.randn(6,4)
columns=['A','B','C','D']

df1 = pd.DataFrame(num_arr,index=dates,columns=columns)
df1


# In[23]:


import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')

ts = pd.Series(np.random.randn(50),index=pd.date_range('today',periods=50))
ts = ts.cumsum()
ts.plot()


# In[28]:


df =pd.DataFrame(np.random.randn(50,4),index=ts.index,columns=['A','B','C','D'])

df =df.cumsum()
df.plot()
df

