#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Password Classifier 

# Just like any Password Generating Platforms most of them require a password that is only characters. So in this case I am
# going to have it classify each of the categories


# In[5]:


import pandas as pd
import string


# In[15]:


def password_strength(password):
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if has_upper and has_lower and has_digit:
        print("The password", password, " is semi-strong")
    elif password.isalpha():
        print("The password", password, " is weak (contains only letters)")
    elif password.isdigit():
        print("The password", password, " is weak (contains only numbers)")
    else:
        print("The password", password, " is not weak or semi-strong")

# Example usage
password_strength("onlyletters")
password_strength("123456")
password_strength("Mixed123")
password_strength("symbols!@#")
password_strength("anna.ronayne2003@gmail.com")


# In[ ]:




