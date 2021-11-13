from classes.Grocery_List import GroceryList
from classes.database_access import DB_Connect
#Importing libraries
import json
import os
import shutil
import time

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




my_db.executeQuery("INSERT INTO grocery_list(item_name, sales_price, price_paid, item_quantity) VALUES (\'"+
str(f_name) +"\',\'"+ str(l_name) +"\',\'"+str(street_address) +"\',\'"+ str(city)  +"\',\'"+str(state) +"\',\'"+str(zip_code) +"\',\'"+ str(company_name) +
"\',\'"+ phone1 +"\',\'"+ phone2 +"\',\'"+ str(email) +"\')")
