#!/usr/bin/env python
# coding: utf-8

# In[1]:


string=input("Enter a string: ")
vowels=0
consonants=0
for i in string:
    if (i=='a' or i=='e'or i=='i' or i=='o' or i=='u'or i=='A' or i=='E'or i=='I' or i=='O' or i=='U' ):
        vowels=vowels+1
else:
    consonants=consonants+1
print("The number of vowels is: ",vowels)
print("The number of consonants is: ",consonants ) 


# In[ ]:




