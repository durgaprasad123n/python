#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# # Number Guessing Game

# In[2]:


jackpot = random.randint(1,125)
guess = int(input('Enter the Number'))
c = 1
while guess != jackpot:
    if guess < jackpot:
        print('Guess higher number')
    else:
        print('Guess lower number')
    guess = int(input('Enter the Number'))
    c+=1
print('correct')
print('you took', c,'attempts')


# In[ ]:




