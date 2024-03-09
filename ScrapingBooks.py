#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# Here is how you can scrape off from a webiste, but its important to have thepermissions of the websitye before scraping. In this example I have used a website that was solely made for the purpose of scraping.

# In[ ]:





# In[3]:


result = requests.get("https://example.com/")


# In[4]:


type(result)


# In[6]:


result.text


# In[2]:


import bs4


# In[8]:


soup = bs4.BeautifulSoup(result.text, "lxml")


# In[9]:


soup


# In[13]:


soup.select('title')


# In[14]:


soup.select('p')


# In[17]:


soup.select('title')[0].getText()


# In[19]:


res = requests.get("https://en.wikipedia.org/wiki/Texas_A%26M_University")


# In[20]:


soup = bs4.BeautifulSoup(res.text, "lxml")


# In[21]:


soup


# In[24]:


soup.select('.vector-toc-contents')[0]


# In[3]:


res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")


# In[5]:


soup = bs4.BeautifulSoup(res.text, 'lxml')


# In[6]:


soup


# In[8]:


soup.select('img')


# In[9]:


soup.select('img')[0]


# In[14]:


soup.select('.infobox')


# In[ ]:




