#!/usr/bin/env python
# coding: utf-8

# # Array Manipulation
# 

# In[2]:


import numpy as np
a = np.arange(9)
print('the original array:')
print(a)
print()
b=a.reshape(3,3)
print("the modified array")
print(b)


# In[3]:


print(b.flatten())


# In[4]:


b.flatten(order="F")


# In[5]:


a = np.arange(12).reshape(4,3)
a


# In[6]:


np.transpose(a)


# In[9]:


b = np.arange(8).reshape(2,4)
b


# In[16]:


c = b.reshape(2,2,2)
c


# In[15]:


np.rollaxis(c,2,1)


# In[ ]:


np.swapaxis(c,1,2)


# # Numpy Arithmetic operator
# 

# In[31]:


a = np.arange(9).reshape(3,3)
a


# In[24]:


b = np.array([10,1000,12])
b


# In[25]:


np.add(a,b)


# In[32]:


np.subtract(a,b)


# In[30]:


np.multiply(a,b)


# In[29]:


np.divide(a,b)


# Slicing

# In[34]:


a = np.arange(20)
a


# In[35]:


a[4:]


# In[36]:


a[:4]


# In[37]:


a[5]


# In[39]:


s = slice(2,9,3)
a[s]


# ## Iterrating over array 

# In[44]:


a= np.arange(0,45,5)
a= a.reshape(3,3)
a


# In[45]:


for x in np.nditer(a):
    print(x)


# # iteration order

# # Joining arrays

# In[49]:


a = np.array([[1,2],[3,4]])
print('first array')
print(a)
b = np.array([[5,6],[7,8]])
print('second array')
print(b)
print('\n')
print('joinng two arrays')
print(np.concatenate((a,b)))
print('\n')
print('joinng two arrays along axis 1') 
print(np.concatenate((a,b),axis = 1))


# # Historgram

# In[51]:


from matplotlib import pyplot as plt
a = np.array([20,87,45,4,53,45,87,68,15,78,11,12,54,85,36])
plt.hist(a, bins =[0,20,40,60,80,100])
plt.title("Mishtrogram")
plt.show()


# # Numpy Practice Example

# In[53]:


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,3*np.pi,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show

