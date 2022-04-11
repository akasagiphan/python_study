#!/usr/bin/env python
# coding: utf-8

# In[25]:


import random

check = True
current_number = 0
if random.randint(0,1) == 0:
    current_player = "human"
else:
    current_player = "computer"
print(f"The starting player is: the {current_player}")
print(f"The starting number is: {current_number}")
print("------------------------------------------")

while current_number <= 21:
    if current_player == "human":
        print("It is your turn.")
        print("------------------------------------------")
        player_choice = ""
        while player_choice not in ("1","2","3"):
            player_choice = str(input("Input a value of your choice between 1/2/3: "))
        else:            
            player_choice = int(player_choice)
            current_number += player_choice
            print(f"The current number has become: {current_number}")
            if current_number >= 21:
                print("******************************************")
                print("The computer won. The human player has lost.")
                print("******************************************")
            else:
                print("------------------------------------------")
                current_player = "computer"
    else:
        print("It is the computer's turn.")
        print("------------------------------------------")
        computer_choice = 0
        while computer_choice not in (1,2,3):
            computer_choice = random.randint(1,3)
        else:
            print(f"The computer has chosen the value of {computer_choice}.")
            current_number += computer_choice
            print(f"The current number has become: {current_number}")
            if current_number >= 21:
                print("******************************************")
                print("Congratulations! The human player has won!")
                print("******************************************")
            else:
                print("------------------------------------------")
                current_player = "human"

