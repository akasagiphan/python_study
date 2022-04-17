#!/usr/bin/env python
# coding: utf-8

# In[34]:


expenses = []
cont = True

def add_item(myTempList, item):
    myTempList.append(item)
    
def find_index_item(myTempList, item_name):
    result = -1
    length = len(myTempList)
    for i in range(length):
        if myTempList[i]['name'] == item_name:
            result = i
    return result

def remove_item(myTempList, item_name):
    if find_index_item(myTempList, item_name) > -1:
        del myTempList[find_index_item(myTempList, item_name)]
    else:
        print(item_name + " not in list")
        
print("Your initial expenses:", expenses)
print("----------------------")
while cont == True:
    print("Do you want to modify expenses list? (y/n)")
    cont_check = str(input("Type y or n: "))
    while cont_check not in ("y","n"):
        cont_check = str(input("Wrong input. Type y or n only: "))
    print("----------------------")
    if cont_check == "y":
        print("What do you want to do?\n"                "1. Add\n"                 "2. Remove")
        option = str(input("Select option 1 or 2: "))
        while option not in ("1","2"):
            option = str(input("Wrong input. Type 1 or 2 only: "))
        option = int(option)
        print("----------------------")
        name_input = input("Item name: ")
        if option == 1:
            cost_input = int(input("Item cost: "))
            date_input = input("Date: ")
            item = {'name': name_input, 'cost':cost_input, 'date':date_input}
            add_item(expenses, item)
            print("----------------------")
            print("Your expenses: ", expenses)
        elif option == 2:
            remove_item(expenses, name_input)
            print("----------------------")
            print("Your expenses: ", expenses)
        else:
            print("Invalid input")
        print("----------------------")
    else:
        cont = False
        print("Program ended.")
        print("Your final expenses: ", expenses)

