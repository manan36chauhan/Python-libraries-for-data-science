#!/usr/bin/env python
# coding: utf-8

# # MATPLOTLIB 

# In[23]:


from matplotlib import pylab
import matplotlib.pyplot as plt
import pandas as pd
print(pylab.__version__)


# In[22]:


import numpy as np
x =np.linspace(0,10,25)
y =x * x + 2
print(x)
print(y)


# In[24]:


pylab.plot(x,y, 'r')


# In[25]:


pylab.subplot(1,2,2)
pylab.plot(x,y, 'r--')
pylab.subplot(1,2,2)
pylab.plot(y,x, 'g*-')


# # Draw Radar Chart
# 

# In[26]:



fig = plt.figure(figsize=(6,6))
ax = fig.add_axes([0.0,0.0,1,1], polar=True)

t = np.linspace(0,2 * np.pi, 100)
ax.plot(t,t*2, color='blue',lw=3)
ax.plot(t,t*3, color='red',lw=5)
ax.plot(t,t*5, color='yellow',lw=3)


# In[28]:


from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(14,6))

ax=fig.add_subplot(2, 2, 1, projection='3d')
ax=plot_surface(X, Y, Z, rstride=4, cstride=4,linewidth=0)


# # pop pro
# 

# In[35]:


import matplotlib.pyplot as plt
languages = 'Python','Java','Ruby','C','C#','PHP'
popularity = [22.2,17.3,8.9,7.7,6.7]
colors =["#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd","#8c564b"]


# In[48]:


explode = (0.1,0,0,0,0,0)
plt.pie(x,popularity, labels=languages ,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)

