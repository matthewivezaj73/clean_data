from classes.Grocery_List import GroceryList
from classes.database_access import DB_Connect
#Importing libraries
import json
import os
import shutil
import time

#Creating an instance of the class.
my_list = GroceryList("Carrots", 2.99, 2.50, 20)


#Creating a list of groceries available.


my_db.executeQuery("INSERT INTO crm_data(f_name, l_name, address, city, state, zip, company, primary_phone, secondary_phone, email_address) VALUES (\'"+
str(f_name) +"\',\'"+ str(l_name) +"\',\'"+str(street_address) +"\',\'"+ str(city)  +"\',\'"+str(state) +"\',\'"+str(zip_code) +"\',\'"+ str(company_name) +
"\',\'"+ phone1 +"\',\'"+ phone2 +"\',\'"+ str(email) +"\')")
