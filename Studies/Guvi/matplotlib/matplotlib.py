#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install matplotlip


# In[6]:


import matplotlib as plt
#start from this
from matplotlib import pyplot as plt
plt.plot([4,1,8,5])


# In[7]:


plt.plot([2500.4800,600.59,9000])


# In[8]:


from matplotlib import pyplot as stats


# In[11]:


stats.plot([20,40,50,20,90])


# In[13]:


stats.xlabel('x axis')
stats.xlabel('y axis')
stats.title('my first title')
stats.plot([1,2,3,4,5,6],[10,20,30,40,50,60])
stats.show()


# In[18]:


stats.xlabel('x axis')
stats.xlabel('y axis')
stats.title('my first title')
stats.plot([1,2,3,4,5,6],[10,20,30,40,50,60])
stats.grid()
stats.show()


# In[49]:


x = [1,2,3,4,5,6]
y = [21,11,9,4,12,11,15]
stats.plot([x,y])
stats.show()


# In[20]:


#bar chart show one side numerical another side alphabetical
plt.bar(["apple","orange","pine"],(20,60,80))


# In[26]:


#add colour
stats.bar(["apple","orange","pine"],[20,60,80],color="r")


# In[32]:


#add colour and alignment
stats.bar(["apple","orange","pine"],[20,60,80],color="g", align="edge" , width=0.2)


# In[34]:


#horizontal bar #BAR(h)add h for horizontal
stats.barh(["apple","orange","pine"],[20,60,80],color="g", align="edge" )


# In[38]:


#pie chart
stats.pie([23,54,84,90])
stats.show()


# In[44]:


#pie chart with label
stats.pie([23,54,84,90],labels=["orange","apple","pineapple","papaya"])
stats.show()


# In[46]:


#pie char with lable and own colour
stats.pie([23,54,84,90],labels=["orange","apple","pineapple","papaya"],colors=["r","g","b","y"])
stats.show()


# In[48]:


#pie char with lable and own colour and #explode
stats.pie([23,54,84,90],labels=["orange","apple","pineapple","papaya"],colors=["r","g","b","y"],explode=(0.2,0.2,0.2,0.2))
stats.show()


# In[ ]:




