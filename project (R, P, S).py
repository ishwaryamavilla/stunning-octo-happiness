#!/usr/bin/env python
# coding: utf-8

# In[16]:


def takeplayerInput():
    player = "blank"
    while not( player.lower() == "r" or player.lower() == "p" or player.lower() == "s"):
        player = input("enter R | P| S")
    return player.lower()


# In[17]:


takeplayerInput()


# In[18]:


import random

def getbotInput():
    lst = ['r','s','p']
    return random.choice(lst)


# In[19]:


getbotInput()


# In[20]:


def checkwinner(player , bot):
    if player =='r' and bot == 'r':
        return "draw"
    elif player =='r' and bot =='s':
        return "player"
    elif player =='r' and bot =='p':
        return "bot"
    elif player =='s' and bot =='s':
        return "draw"
    elif player =='s' and bot =='r':
        return "bot"
    elif player =='s' and bot =='p':
        return "player"
    elif player =='p' and bot =='s':
        return "bot"
    elif player =='p' and bot =='r':
        return "player"
    else:
        return "draw"


# In[23]:


checkwinner(player ='s',bot ='p')


# In[30]:


def rockpaperscissor():
    endgame= "n"
    player_score = 0
    bot_score = 0
    while endgame.lower() != "y":
        ply = takeplayerInput()
        bt = getbotInput()
        winner = checkwinner(player = ply , bot = bt)
        if winner == "player":
            player_score +=2
        elif winner =="bot":
            bot_score +=2
        else:
            player_score +=1
            bot_score +=1
            
        print("---scoreboard---")
        print("-player-",player_score)
        print("-bot-",bot_score)
        
        endgame = input("you want to end y/n")


# In[31]:


rockpaperscissor()


# In[ ]:




