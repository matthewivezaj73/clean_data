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




my_db.executeQuery("INSERT INTO crm_data(item_name, sales_price, price_paid, item_quantity) VALUES (\'"+
str(f_name) +"\',\'"+ str(l_name) +"\',\'"+str(street_address) +"\',\'"+ str(city)  +"\',\'"+str(state) +"\',\'"+str(zip_code) +"\',\'"+ str(company_name) +
"\',\'"+ phone1 +"\',\'"+ phone2 +"\',\'"+ str(email) +"\')")
