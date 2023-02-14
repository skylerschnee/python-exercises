#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json

with open("atm_data.json", "r+") as f:
    d = json.load(f)    
    pin = input("Please Enter Your Pin")
    

def main_menu():
    
        if pin in d:

            print("\tWelcome to your Terminal Checkbook, " + d[pin]["name"] + "!")
            print("\n\t\tMain Menu")
            print("\t1. View balance")
            print("\t2. Record a debit")
            print("\t3. Record a credit")
            print("\t4. View and search transaction history")
            print("\t5. Modify a transaction")
            print("\t6. Exit")

        menu_select = input("\nPlease make a selection (1 - 6) ")
        allowables = ["1", "2", "3", "4", "5", "6"]
        
        if menu_select not in allowables:
            print("The selection provided is invalid.")
            main_menu()

        elif int(menu_select) == 1:
            show_bal()

        elif int(menu_select) == 2:
            add_debit()

        elif int(menu_select) == 3:
            add_credit()

        elif int(menu_select) == 4:
            show_hist()

        elif int(menu_select) == 5:
            mod_tx()

        elif int(menu_select) == 6:
            exit()

def show_bal():
    print("Your current account balance is $ " + d[pin]["amt"])
    again = input("Would you like to continue? Yes or No\n")
    if again.lower() == "yes" or again.lower() == "y":
        main_menu()
    elif again.lower() == "no" or again.lower() == "n":
        exit()
    else:
        print("***Invalid repsonse*** Try again...")
        show_bal()
    
def add_debit():
    debit = input("What is the total debit? ")
    if debit.isdigit() == False:
        print("***Invalid repsonse*** Try again...")
        add_debit()
    elif float(debit) > float(d[pin]["amt"]):
        print("Insufficient Funds")
        add_debit()
    else:
        new_bal = float(d[pin]["amt"]) - float(debit)
        d[pin]["amt"] = str(new_bal)
        print(f"Debit successfully recorded\nRemaining Amount is $ " + d[pin]["amt"])
        with open('atm_data.json', 'w') as k:
            json.dump(d,k)
        
        again = input("Would you like to continue? Yes or no\n")
        if again.lower() == "yes" or again.lower() == "y":
            main_menu()
        elif again.lower() == "no" or again.lower() == "n":
            exit()
        else:
            print("***Invalid repsonse*** Try again...")
        add_debit()
        
def add_credit():
    credit = input(f"What is the total credit? ")
    if credit.isdigit() == False:
        print("***Invalid repsonse*** Try again...")
        add_credit()
    else:
        new_bal_cred = float(d[pin]["amt"]) + float(credit)
        d[pin]["amt"] = str(new_bal_cred)
        print("Credit successfully recorded!\nUpdated Amount is $ " + d[pin]["amt"])
        with open("atm_data.json", "w") as k:
            json.dump(d,k)
            
        again = input("Would you like to continue? Yes or no\n")
        if again.lower() == "yes" or again.lower() == "y":
            main_menu()
        elif again.lower() == "no" or again.lower() == "n":
            exit()
        else:
            print("***Invalid repsonse*** Try again...")
        add_credit()
        
def show_hist():
    print("Feature under construction! ")
    again = input("Would you like to continue? Yes or no\n")
    if again.lower() == "yes" or again.lower() == "y":
        main_menu()
    elif again.lower() == "no" or again.lower() == "n":
        exit()
    else:
        print("***Invalid repsonse*** Try again...")
        show_hist()
        
def mod_tx():
    print("Feature under construction! ")
    again = input("Would you like to continue? Yes or no\n")
    if again.lower() == "yes" or again.lower() == "y":
        main_menu()
    elif again.lower() == "no" or again.lower() == "n":
        exit()
    else:
        print("***Invalid repsonse*** Try again...")
        mod_tx()
        
main_menu()


# In[ ]:





# In[ ]:




