#!/usr/bin/env python
# coding: utf-8

# In[1]:


m = 5
c = -1
x = [0, 1, 2, 3, 4, 5, 6]


# In[2]:


import numpy as np


# In[3]:


X = np.array(x)
Y = m*X + c


# In[5]:


print(Y)


# In[9]:


import matplotlib.pyplot as plt


# In[11]:


plt.scatter(X,Y)
plt.show()


# In[ ]:




