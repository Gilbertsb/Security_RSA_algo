#!/usr/bin/env python
# coding: utf-8

# In[6]:


# SHA1- hash algorithms.

import hashlib


# initializing string
str = "Gilbert is doing the work"

# encoding string using encode()
# then sending to SHA1()
result = hashlib.sha1(str.encode())

# printing the equivalent hexadecimal value.
print("The the text is  : Gilbert is doing the work ")
print("Hashing for text is  : ",result.hexdigest())


# In[ ]:





# In[ ]:




