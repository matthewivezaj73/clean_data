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
    action = input("Please enter I if you would like to import a new list to the table to add more groceries."+
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
        #Saving all unsaved changes to the database.
        my_db.conn.commit()

    #Added a case for if the user selects r.
    elif action.lower() == "r":
        #Setting flags to false
        data_question_ok = False
        #Testing for what the user would like to do.
        while not data_question_ok:  
            #Asking the user what they would like to do.
            data_question = input("Would you like to edit the grocery_list (please enter \'grocery_list\' (without single quotes), respectively) "+
            "If you would like to delete a record enter the word \"delete_grocery\" or "+
            "\"delete_mailings\" without quotes (or enter Q to go back to the main menu)?")
            #If the user enters delete_crm.
            if data_question.lower() == "delete_grocery":
                #Creating a new, blank list.
                valid_ids = []
                #Setting flags to false.
                del_id_ok = False
                #Testing for the id.
                while not del_id_ok:  
                    #Asking the user for the crm_id.
                    grocery_id = input("Please enter the crm_id for whose row you "+
                    "would like to delete or enter q to quit (takes you back to the main menu): ")
                    #Checking if the id enetered is a digit, else returns false.             
                    if grocery_id.isdigit():
                        #selecting crm_id's from the crm_data where crm_id = the value inputted for crm_id.
                        item_id = my_db.executeSelectQuery("SELECT item_id FROM grocery_list WHERE item_id ="+"\'"+grocery_id +"\'") 
                        #Looping through the list of IDs.
                        for v_id in my_id:
                            #Specifying the list to only grab the ID in the dictionary.
                            for my_new_id in v_id.values():
                                #Appending each id to the valid_ids to the valid_ids list (making it an str
                                # so that it can be appended, I could not append as it without running into issues).
                                valid_ids.append(str(my_new_id))
                        #Checking to see if the id is not in the list of ids.
                        if grocery_id not in valid_ids:
                            #Notifying the user that the ID is incorrect.
                            print("\'"+grocery_id + "\' is an invalid ID.")
                        #If else, just move on.
                        else:
                            #Setting flags to break out of the loop.
                            del_id_ok = True
                            question_ok = False
                    #If the user enters q.
                    elif grocery_id.lower() == "q":
                        #Breaking out of the loop if the user chooses to quit.
                        del_ok = True
                        del_id_ok = True
                        question_ok = True
                    else:
                        #Notifying the user that the ID entered was invalid.
                        print("\'"+grocery_id+"\'"+" is an invalid id!")
                        #Setting del_id_ok to false to continue with asking for an id.
                        del_id_ok = False
                #Testing for the question and then executing the save to the database.
                while not question_ok:
                    #Setting a new flag to trap this question
                    not_question_ok = False
                    #Testing for the question
                    while not not_question_ok:
                        #Asking the user if they would like to delete the specified record.
                        question = input("Are you sure you want to delete item_id: " +grocery_id+"\nenter Y/N (Y for Yes and N for No) to confirm: ")
                        #Creating a select statement that only takes the crm_id (The reason I have this set as a private variable rather than global 
                        # is because when I had it set as global, I ran into a bug that would not accept a valid ID).
                        my_id = my_db.executeSelectQuery("SELECT item_id FROM grocery_list")
                        #If the user enters y, then delete the id.
                        if question.title() == "Y":         
                            #Applying the deletion to the Python_Database_Assignment table.
                            my_db.executeQuery("DELETE FROM grocery_list WHERE item_id =" + "\'"+grocery_id+"\'")
                            question_ok = True
                            not_question_ok = True
                        #If the user selects n, then break.
                        elif question.title() == "N":
                            #Breaking out of the loop if the user changes there mind.
                            del_id_ok = False
                            question_ok = True
                            break
                        else:
                            #Telling the user why the option was invalid.
                            print("\'"+question + "\'"+" is an invalid option, please try again!")
                    #Testing if del_id_ok is false. 
                    if del_id_ok:
                        #Creating a new list.
                        valid_ids = []
                        #Looping through each dictionary in the list.
                        for v_id in my_id:
                            #Specifying the list to only grab the ID in the dictionary.
                            for my_new_id in v_id.values():
                                #Appending each id to the valid_ids list (making it an str so that it can be 
                                # appended, I could not append as it without running into issues).
                                valid_ids.append(str(my_new_id))
                        #Checking to see if an ID is not in the list.
                        if item_id not in valid_ids:
                            #Notifying the user that the ID is incorrect.
                            print("Invalid ID was entered, taking you back to the delete menu!")
                            #Setting flag to true to take the user back to the delete menu.
                            del_id_ok = False
                            question_ok = True
                        else:
                            #Saving work
                            my_db.conn.commit()
                            #Setting flags to Take the user back to the delete menu.
                            del_id_ok = False
                            question_ok = True
                    else:
                        #Setting a flag to tell the program to keep running the loop.
                        del_id_ok = False

    #Added a case for if the user selects e.
    elif action.lower() == "e":
        #Setting a flag to false to for the test question.
        while not mail_question_ok:
            #Setting flag to true.
            data_question_ok = True
            #Asking the user for the column that they would like to edit.
            mailings_column = input("Which column of the grocery_list table "+
            "would you like to edit?\n-item_name\n- sales_price\n- price_paid\n- item_quantity\n- Q to quit:  ")
            #If the user enters 'name'
            if mailings_column.lower() == "name":
                #Setting flag to false so that the name can be tested.
                first_name_ok = False
                #Running a loop to get and evaluate the first name.
                while not first_name_ok: 
                    #Asking for the user to input the first name, then evaluating it. I used the if 
                    # else because it wasn't working with only asking for the info and calling the check method. 
                    first_name_value = input("Please enter the customer's first name (this can only "+
                    "contain letters, a single quote, and a hyphen): ").replace("'","\\'")
                    #Evaluating the first name.
                    first_name_ok = my_customer.customer_name_check(first_name_value)   
                #Setting a flag to false.
                last_name_ok = False
                #Running a loop to get and evaluate the last name.
                while not last_name_ok:
                    #Asking for the user to input the first name, then evaluating it. I used the if 
                    # else because it wasn't working with only asking for the info and calling the check method. 
                    last_name_value = input("Please enter the customer's last name (this can only "+
                    "contain letters, a single quote, and a hyphen): ").replace("'","\\'")
                    #Evaluating the last name.
                    last_name_ok = my_customer.customer_name_check(last_name_value)   
                #Creating a value for the first, last name
                customer_name_value = f"{first_name_value} {last_name_value}"
                #Then updating the mailings database and saving the changes.
                my_db.executeQuery("UPDATE Mailings SET name=" + 
                "\'"+ customer_name_value +"\'"+" WHERE mail_id =" +"\'"+mail_id+"\'")
                #Setting a set of flags to true.
                crm_data_ok = True
                mail_id_ok = True
                mail_question_ok = False
            #If the user enters q.
            elif mailings_column.lower() == "q":
                #Setting flags to true to break out of the loop.
                data_question_ok = False
                del_ok = True
                mail_question_ok = True
                mail_id_ok = True  
            #If the user enters company.
            elif mailings_column.lower() == "company":
                #Setting flag so that we can perform a test.
                company_ok = False
                #Testing for the company name.
                while not company_ok: 
                    #Ask for the user for the company name, then evaluating it. I used 
                    # the if else because it wasn't working with only asking for the info and calling the check method. 
                    company = input("Please enter the company name "+
                    "(this can include any value(s)!)").replace("'","\\'")
                    #Evaluating the value passed into the company variable.
                    company_ok = my_customer.company_name_check(company)
                #Then updating the mailings database and saving the changes.
                my_db.executeQuery("UPDATE Mailings SET company=" +
                "\'"+ company +"\'"+" WHERE mail_id =" +"\'"+mail_id+"\'")
                #Setting flags to true
                mail_id_ok = False
                crm_data_ok = True
            #If the user enters address.


