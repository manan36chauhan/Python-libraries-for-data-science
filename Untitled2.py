#!/usr/bin/env python
# coding: utf-8

# In[29]:


import numpy as np


# In[30]:


a=np.array([1,2,3])
print(a)


# In[31]:


a[0]


# In[33]:


import time
import sys


# In[34]:


b=range(1000)
print(sys.getsizeof(5)*len(b))


# In[35]:


c = np.arange(1000)
print(c.size*c.itemsize)


# In[36]:


size = 100000


# In[37]:


L1 = range(size)
L2 =  range(size)
A1 = np.arange(size)
A2 = np.arange(size)


# In[53]:


start = time.time()
result = [(x+y) for x,y in zip(L1, L2)]
print("python list took",(time.time()-start)*1000)


# # NUMPY tutorials
# 

# In[45]:


start = time.time()
result = A1+A2
print("numpy array took",(time.time()-start)*1000)


# In[56]:


a = np.array([[1,2],[3,4],[5,6]])
a


# In[57]:


a.ndim


# In[58]:


a.itemsize


# In[59]:


a.shape


# In[61]:


a.itemsize


# In[ ]:




