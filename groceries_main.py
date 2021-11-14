#Importing modules from the classes folder.
from classes.Grocery_List import GroceryList
from classes.database_access import DB_Connect
#Importing libraries
import json
import os
import shutil
import time
#Creating the list of items.
my_groceries = ['Gallon of milk', 'Carton of eggs', 'Cheese block', 'Yogurt', 'Apples', 'Bananas', 'Carrots', 'Tomatoes', 'Potatoes', 'Broccoli', 'Meat', 
'Chicken breast', 'Fresh fish', 'frozen fish', 'Grains', 'Loaf of bread', 'Dry pasta', 'Brown rice', 'Couscous', 'Tomato sauce', 'Peanut butter', 'Granola bars', 
'Extra protein', 'Nuts', 'Dried beans', 'canned beans']
#Creating a dictionary of prices for each item.
my_prices = {'Gallon of milk':1.99, 'Carton of eggs': 2.88, 'Cheese block': 3.00, 'Yogurt': .99, 'Apples': .89, 
'Bananas':1.21, 'Carrots':1.09, 'Tomatoes':3.99, 'Potatoes':2.89, 'Broccoli':2.33, 'Meat':3.76, 'Chicken breast':4.32, 'Fresh fish':2.99, 'frozen fish':2.95, 'Grains':1.88, 
'Loaf of bread':1.32, 'Dry pasta':1.00, 'Brown rice':3.20, 'Couscous':2.95, 'Tomato sauce': 1.99, 'Peanut butter':2.00, 'Granola bars':1.44,'Extra protein':3.99, 'Nuts':2.50, 'Dried beans':3.00, 'canned beans':1.99}

#Creating an instance of the class.
my_list = GroceryList("Carrots", 2.99, 2.50, 20)
#Creating a connection to the database
my_db = DB_Connect('root','','python_projects')
#Selects all of the data from the grocery list table.
list_data = my_db.executeSelectQuery("SELECT * FROM grocery_list")
#Entering a flag.
not_list = False
#Testing for the user's input.
while not not_list:
    #Asking the user what they would like to do.
    action = input("Please enter C if your would like to create the list."+ 
    "\nPlease enter I if you would like to import a new list to the table to add more groceries."+
    "\nPlease enter A if you would like to add to the list\nPlease enter R if you would like to rremove to the list\n"+
    "Please enter S if you would like to save the list\nPlease enter E if you would like to exit")
    #Handling the case where the user selects a for add.
    if action.lower() == "a":
        #Creating a flag.
        not_add = False
        #Testing for the user's input.
        while not not_add:
            #Asking the user what the name of the item is.
            item_name = input("Please enter the name of the item: ")
            #Validating the name of the item entered and breaking out of the list if it is valid.
            not_add = my_list.add_item(item_name)
        #Creating a flag.
        not_sales = False
        #Testing for the user's input.
        while not not_add:
            #Asking the user what the sales price of the item .
            item_name = input("Please enter the sales price of the item: ")
            #Validating the name of the item entered and breaking out of the list if it is valid.
            not_add = my_list.add_item(item_name)
        my_db.executeQuery("INSERT INTO grocery_list(item_name, sales_price, price_paid, item_quantity) VALUES (\'"+
        str(item_name) +"\',\'"+ str(sales_price) +"\',\'"+str(price_paid) +"\',\'"+ str(item_quantity)  +"\')")
    #Added a case for if the user selects i.
    elif action.lower() == "i":
    #Added a case for if the user selects c.
    elif action.lower() == "c":
    #Added a case for if the user selects s.
    elif action.lower() == "s":
    #Added a case for if the user selects r.
    elif action.lower() == "r":
    #Added a case for if the user selects e.
    elif action.lower() == "e":


