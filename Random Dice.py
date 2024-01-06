#!/usr/bin/env python
# coding: utf-8

# In[1]:


### <div align='center'> Random Number Generator </div>
# For this project, I just wanted to create a simplistic die roller that rolls the amount of times, that way if needed for 
# for a board game that needed a specific amount of die that the player would be able to use this pseudo random number generator
# in order to get the results


# In[2]:


import random


# In[3]:


# random 6 sided dice roller.
dice_roll6lower = 1
dice_roll6upper = 6

number_of_rolls = int(input("How many times do you want to roll the dice?"))

for _ in range(number_of_rolls):
    roll_6 = random.randint(dice_roll6lower, dice_roll6upper)
    print(roll_6)


# In[6]:


#Updated constraints 
dice_roll_lower = int(input("Enter the lower bound for the dice rolls: "))
dice_roll_upper = int(input("Enter the upper bound for the dice rolls: "))

number_of_rolls = int(input("How many times do you want to roll the dice? "))
if(dice_roll_lower > dice_roll_upper):
    print("This wont roll")
else:
    for _ in range(number_of_rolls):
        roll_result = random.randint(dice_roll_lower, dice_roll_upper)
        print(roll_result)


# In[ ]:





# In[ ]:




