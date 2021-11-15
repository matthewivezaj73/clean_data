#Import unittest Library.
import unittest
#Import all methods from InventoryItem in the classes folder.
from classes.Grocery_List import GroceryList
class TestCustomerClass(unittest.TestCase):
    """
    TestCase unittest testing for 
    the TestCustomerClass Class.
    Running the following tests: 
    assertTrue/assertFalse 
    """
    def setUp(self):
        """
        Create an instance of the Grocery_List class for testing all class methods.
        """
        #Creating an instance of the Validation class and adding a list.
        self.Grocery_List = GroceryList()
    def test_add_item_check_false(self):
        """
        """
        #Creating a list of bad addresses
        baditems = ["!","[]}{>","!a","a!","Attlewood@","]Attlew[ood&","Attlewood&","432 Attlewood{","}432 Attlewood", "?Shall{owwood]","@a l a n w o o d #","@A T T L E W O O D","!A T T L E W O O D", "A T T L E W O O D@", "A* T T L! E W# O O D@", "[Shallowwood;","[S","&Sha@llowwood;","@","@#","@*#","@latter# $Grove@","<Shallowwood> 324","$324 shallowwood","$324 #shallowwood","$324 shallowwood(*%"]
        #Checkings for each string in the list.
        for bitems in baditems:
            #Evaluating each string.
            self.assertFalse(self.Grocery_List.add_item(bitems))
    def test_check_price_true(self):
        """
        """
        #Creating a list of good addresses
        gooditems = ["4123.21"," 3212.00","21.12","0.21","0.1","0.00"]
        #Checkings for each string in the list.
        for gitems in gooditems:
            #Evaluating each string.
            self.assertTrue(self.Grocery_List.add_item(gitems))
    def test_check_price_false(self):
        """
        """
        #Creating a list of bad prices.
        bad_prices = ["!4123.21","321200"," 21.12"," 21.12 ","21.12 ","@0.21%","0.1#"]
        #Checkings for each string in the list.
        for bprices in bad_prices:
            #Evaluating each string.
            self.assertFalse(self.Grocery_List.check_price(bprices)) 
    def test_remove_item_true(self):
        """
        """
        #Creating a list of good prices.
        good_prices = ["Waterford'","Water'ford","\'Waterford","water\'ford","waterford'","Shelby '","' Shelby"," shelby","shelby","shelby township","utic","Shelby Township","Shelby'Township","'Shelby'Township'","ShelbyTownship","shelbytownship","SHELBY","SHELBY "," SHELBY"," SHELBY ","shelby "," shelby"," shelby "," Shelby","Shelby "," Shelby "]
        #Checkings for each string in the list.
        for city in good_city_information:
            #Evaluating each string.
            self.assertTrue(self.Grocery_List.city_information_check(city)) 
    def test_remove_item_check(self):
        """
        """
        #Creating a list of bad company to use in test
        invalid_invalid_company_name_check_list = [" ","  ","   ","    ","     ", "      ","       ","        "]
        #Calling company_name_check and passing home in the arguments
        for company in invalid_invalid_company_name_check_list:
            self.assertFalse(self.Grocery_List.company_name_check(company.strip()))
    def test_valid_company_name_check(self): 
        """
        """
        valid_company_name_check_list = ["$Dollar Store","DollarStore","Dollar Store","Dollar Store#","Dollar Store123","a","a1","1a","dollar store","dollarstore","DOLLAR STORE"," Dollar Store","Dollar Store "," Dollar Store","1dollar3 store","6dollar1 3store2","dollar3 5store2","*dollar1 !store2","(dollar$ !store@","@dollar$ 3store2"]
        #Calling company_name_check and passing home in the arguments
        for company in valid_company_name_check_list:
            #Evaluating the company name method.
            self.assertTrue(self.my_customer.company_name_check(company))
    def test_invalid_customer_name_check(self):
        """
        """
        #Creating a list of valid names to test.
        invalid_names_list = ["!Phil","!Phil#","!Ph#il$","*phil","*phil$","*ph#il^","*PH'IL","*ph'il-","*phi- l","*'ph'il'","!- '%","1phil","1phil7","phil6","4phil'","7phil-","1ph4353il","12345434","7phil$","&$#@((*&%",""," "]
        #Looping through each name in the list.
        for name in invalid_names_list:
            #Evaluating the customer name method.
            self.assertFalse(self.my_customer.customer_name_check(name))
    def test_valid_customer_name_check(self):
        """
        """
        #Creating a list of valid names to test.
        valid_names_list = ["Phil","phil","PHIL","'phil","ph il","PH'IL","phil'","phil-","-phil","'ph- il","-ph'i l","-' "]
        #Looping through each name in the list.
        for name in valid_names_list:
            #Evaluating the customer name method.
            self.assertTrue(self.my_customer.customer_name_check(name))
    def test_invalid_email(self): 
        """
        """
        #Creating a list of bad emails to test.
        invalid_email_list= ["!mary123@mail.com","!mary12@#$3@()$#*&mail.com%","!mary123@mail.com%","mary123@mail.com#","mary123mailcom#","MARY!MAILCOM","#mary123mailcom!","mary!mailcom","mary!gmail.com","$mary123mailcom","^&^*&#!@",""," "]
        #Calling retail_price_check and passing home in the arguments
        for email in invalid_email_list:
            #Evaluating each email in the list.
            self.assertFalse(self.my_customer.email_check(email))
    def test_valid_email(self): 
        """
        """
        #Creating a list of good emails to test.
        valid_email_list= ["mary123mail.com","mary123mail.com","marymail.com","a","i3@","3@3.com","a@","a.",".d","@d","marymailcom","1marymailcom4","4marymailcom","marymailcom6","marrymailcom","marymail","sally73@gmail.com","SALLY73@GMAIL.COM","4marymailr3242com3","9324759872395734","mary123@mail.com"]
        #Calling retail_price_check and passing home in the arguments
        for email in valid_email_list:
            #Evaluating each email in the list.
            self.assertTrue(self.my_customer.email_check(email))
    def test_invalid_phone_check(self): 
        """
        """
        #Creating a list of bad phone numbers to test.
        invalid_phone_check = ["212.599.6363","!2125996363","2125996363!","Tom! Petz*","##Cindy##","a2259a","aaa.bbb.cccc","&$#(&@*(&#$@&(#@*","","jkahdfjhsafkdh","&*#-#&$-#$&*"," ",'&@#($&#42343&($!#(2432&*#(@$$*',"423342432a)","f231213321","d1232(1323h","*123231231","231231213$","^231a23132","g32132123&"]
        #Calling phone_number_check and passing the number in the arguments
        for phone in invalid_phone_check:
            #Evaluating each phone number in the list.
            self.assertFalse(self.my_customer.phone_number_check(phone))
    def test_valid_phone_check(self): 
        """
        """
        #Creating a list of good numbers
        valid_phone_check = ["212-599-6363","212-599-6363","1234567890","123-123-1234","1111111111","-1111111111-","-1112223334-","1231233212--","--1231233212","222-222-2222","7777777777"]
        #Calling phone_number_check and passing the number in the arguments
        for phone in valid_phone_check:
            #Evaluating the phone numbers
            self.assertTrue(self.my_customer.phone_number_check(phone))
    def test_invalid_state_check(self): 
        """
        """
        #Creating a list of bad state checks.
        invalid_state_list= ["M1","dahs","ASG","A","1M","11","!M","m1","A&","1m","!!","!M","M!","","  "," "," M","I "]
        #Calling retail_price_check and passing home in the arguments
        for state in invalid_state_list:
            #Evaluating each value in the list.
            self.assertFalse(self.my_customer.state_information_check(state))
    def test_valid_state_check(self): 
        """
        """
        #Creating a list of good state values.
        invalid_state_list= ["MI","mi","aZ","Az","fw"]
        #Calling retail_price_check and passing home in the arguments
        for state in invalid_state_list:
            #Evaluating each value in the list.
            self.assertTrue(self.my_customer.state_information_check(state))
    def test_invalid_zip_code_check(self): 
        """
        """
        #Creating a list of bad zip code values to test.
        invalid_state_list= ["123m","!423d","12m3","12345678","!123","123!","12!3","123","0","12","as","!","a","wq","as2d","asfd","asfdd","@#","$@#","$#@@","j#@a","j23i","2sd@","@df4","asd1",""," "]
        #Calling retail_price_check and passing home in the arguments
        for state in invalid_state_list:
            #Evaluating each value in the list.
            self.assertFalse(self.my_customer.zip_code_check(state))
    def test_valid_zip_code_check(self): 
        """
        """
        #Creating a list of good values to test.
        valid_zip_code_list= ["1234","4321","12345","1111","11111","1112","2111","2112","21112","31115","21314"]
        #Calling retail_price_check and passing home in the arguments
        for zip_code in valid_zip_code_list:
            #Evaluating each value in the list.
            self.assertTrue(self.my_customer.zip_code_check(zip_code))
