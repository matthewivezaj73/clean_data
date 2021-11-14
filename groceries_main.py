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
        #Truncating the data in the crm_data table.
        my_db.executeQuery("TRUNCATE crm_data")
        #Truncating the data in the Mailings table.
        my_db.executeQuery("TRUNCATE Mailings")
        #Asking the user which database they would like to work with and creating a link to the file. 
        response_ok = False
        #Creating an empty dictionary.
        my_dict = {}
        #Assinging a file path to a variable.
        filename =  "text_files/grocery_list.txt"
        #Creating two blank lists for future use.
        output_content = []
        my_nondup_lines = []
        #Opening the text file to work with.
        with open(filename) as fold:
            #Creating a backup copy of the CSV file before writing a new copy of it.
            for temp_line in fold:
                #Replacing the # in the temp_line with noting.
                temp_line = temp_line.replace('#', "")
                #Making a split at the | character.
                temp_line = temp_line.split("|")
                #Checking to see if the length of the temp_line is equal to 10.
                if len(temp_line) == 10:
                    #If the value at index 0 is first_name, then all we are doing is assigning it a value.
                    if temp_line[0] == "item_name":
                        #Creating a formatted line
                        line = f"{temp_line[0]}, {temp_line[1]}\n"
                    elif temp_line[0] == "item_name":
                        #Creating a formatted line
                        line = f"{temp_line[0]}, {temp_line[1]}, {temp_line[2]}\n"

                    #Else, we will append all other values to a list.
                    elif temp_line[0] == "item_name":
                        #Creating a formatted line
                        line = f"{temp_line[0]}, {temp_line[1]}, {temp_line[2]}, {temp_line[3]}\n"
                        #Appending each line to a list.
                        output_content.append(line)
                    #Handling the case where nothing works
                    else:
                        print("Sorry, but something went wrong.")
                #Else, if the length of the temp_line is not equal to 10.
                else:
                    #Checking to see if the first line is first_name.
                    if temp_line[0] == "item_name":
                        #Creating a formatted line.
                        line = f"{temp_line[0]}, {temp_line[1]}\n"
                    else:
                        #Creating a formatted line.
                        line = f"\"{temp_line[0]}\", \"{temp_line[1]}\", \"{temp_line[2]}\", \"{temp_line[3]}\", \"{temp_line[4]}\", \"{temp_line[5]}\", \"{temp_line[6]}\", \"{temp_line[7]}\", \"{temp_line[8]}\", \"{temp_line[9]}\",  \"{temp_line[10]}\"\n"
                ####BEGIN REMOVAL OF DUPLICATE LINES####
                #Setting a flag
                matched_word = False
                #Looping through every entry in my_nondup_lines
                for my_line in my_nondup_lines:
                    #Checking for the address
                    if temp_line[3] in my_line:
                        #Printing a message so that I am telling the user that I am deleting the customer with a specified address value.
                        print(f"removing a duplicate line with address: {temp_line[3]}")
                        #Setting our flag to true.
                        matched_word = True
                        #Breaking out of the loop
                        break
                #Checking to see if the matched word is true.
                if not matched_word:
                    #Appending each line to the list.
                    my_nondup_lines.append(line)
            #Opening the file for writing/creating if it does not exist.
            with open("text_files/grocery_list.csv","w+") as fawn:
                #Going through each line in the list.
                for line in my_nondup_lines:
                    #Writing each line to the file.
                    fawn.write(line)             

    #Added a case for if the user selects s.
    elif action.lower() == "s":
    #Added a case for if the user selects r.
    elif action.lower() == "r":
    #Added a case for if the user selects e.
    elif action.lower() == "e":


