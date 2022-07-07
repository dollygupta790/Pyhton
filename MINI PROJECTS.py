#!/usr/bin/env python
# coding: utf-8

# # Generating random passwords

# In[3]:


import random

n=int(input('Enter the size of the password you need :'))


def passwordGenerator(n):
    
    lower='abcdefghijklmnopqrstuvwxyz'
    upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number='0123456789'
    special='!@#$%^&*'
    
    password=''
    
   #l=[random.choice(lower),random.choice(upper),random.choice(number),random.choice(special)]
    
    for i in range(n):
        l=[random.choice(lower),random.choice(upper),random.choice(number),random.choice(special)]
        password=password+random.choice(l)
       
    
    return password
print('Your randomly generated password is :',passwordGenerator(n))


# # Rock Paper Scissors

# In[1]:


import random
l=['Rock','Paper','Scissors']
player=False

while player==False:
    computer=random.choice(l)
    
    print('\nChoose anything form here')
    ply=input('Rock Paper Scissors')
    
    print('Player choosed :',ply)
    print('Computer choosed :',computer)
    
    if computer==ply:
        print('Match is draw ....')
    else:
        if computer=='Rock':
            if ply=='Paper':
                print('Computer wins by match')
            else:
                print('Computer wins by match')
        elif computer =='Paper':
            if ply=='Scissors':
                print('Player won the match')
            else:
                print('Player won the match')
        elif computer=='Scissors':
            if ply=='Paper':
                print('Computer won the match')
            else:
                print('Player won the match')

    ch=input('Do want to continue or not ?y/n ->')
    if ch=='n':
        player =True
    else:player    

