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
        Create an instance of the Customer class for testing all class methods.
        """
        #Creating an instance of the Validation class and adding a list.
        self.my_customer = Customer()
    def test_address_check_false(self):
        """
        Test to see if address is not valid
        Tests Ran: assertFalse
        assertFalse - Checks to see whether the 
        address passed will be contains characters that are not normally allowed,

        Such as the following:
        ! " ' @ $ % ^ & * _  = + < >  ? ; [ ] { }, if it does, return true.
        """
        #Creating a list of bad addresses
        bad_addresses = ["!","[]}{>","!a","a!","Attlewood@","]Attlew[ood&","Attlewood&","432 Attlewood{","}432 Attlewood", "?Shall{owwood]","@a l a n w o o d #","@A T T L E W O O D","!A T T L E W O O D", "A T T L E W O O D@", "A* T T L! E W# O O D@", "[Shallowwood;","[S","&Sha@llowwood;","@","@#","@*#","@latter# $Grove@","<Shallowwood> 324","$324 shallowwood","$324 #shallowwood","$324 shallowwood(*%"]
        #Checkings for each string in the list.
        for address in bad_addresses:
            #Evaluating each string.
            self.assertFalse(self.my_customer.address_check(address))
    def test_address_check_true(self):
        """
        Test to see if the address is valid
        Tests Ran: assertTrue
        assertTrue - Checks to see if The address 
        is comprised primarily of alphanumeric characters,
        but must not contain any of the following characters: 
        ! " ' @ $ % ^ & * _  = + < >  ? ; [ ] { }
        """
        #Creating a list of good addresses
        addresses = ["4123 Shallow Grove DR "," 4123 Shallow Grove DR"," 4123 Shallow Grove DR ","shallow","23132","3","34","342","3dsf2","a23s","shallow grove","shallow grove 4324234","SHALLOW GROVE","SHALLOW","4123 SHALLOW GROVE DR","4123 Shallow Grove DR 132","4123 shallow grove dr"]
        #Checkings for each string in the list.
        for address in addresses:
            #Evaluating each string.
            self.assertTrue(self.my_customer.address_check(address))
    def test_city_information_check_false(self):
        """
        Test to see if the city name is invalid.
        Tests Ran: 
        assertFalse - Checks to see if the city name is not 
        in the city bad name. Tests the city names in bad_city_information 
        list as a list of bad names to see if it contains characters that are not normally allowed.
        """
        #Creating a list of bad city info.
        bad_city_information = ["1Waterford!'","@ waterford","Pontiac!","#Pontiac!","%Pontiac","231 waterford!","$231 waterford!","@321 waterford","321 waterford@",")321( waterford",")321( waterford@",")321( #waterford%","321 #waterford$","@w a t e r f o r d","@w a t e r f o r d^","w a t e r f o r d^"]
        #Checkings for each string in the list.
        for city in bad_city_information:
            #Evaluating each string.
            self.assertFalse(self.my_customer.city_information_check(city)) 
    def test_city_information_check_true(self):
        """
        Test to see if the city name is valid.
        Tests Ran: 
        assertTrue - Checks to see if the name that is comprised of anything so it can be validated.
        Tests the names in good_city_information list as a list of potential good names.
        """
        #Creating a list of good city info to use in test
        good_city_information = ["Waterford'","Water'ford","\'Waterford","water\'ford","waterford'","Shelby '","' Shelby"," shelby","shelby","shelby township","utic","Shelby Township","Shelby'Township","'Shelby'Township'","ShelbyTownship","shelbytownship","SHELBY","SHELBY "," SHELBY"," SHELBY ","shelby "," shelby"," shelby "," Shelby","Shelby "," Shelby "]
        #Checkings for each string in the list.
        for city in good_city_information:
            #Evaluating each string.
            self.assertTrue(self.my_customer.city_information_check(city)) 
    def test_invalid_company_name_check(self):
        """
        Test to see if the company_name is invalid.
        Test ran: assertTrue.
        assertFalse - Checks to see if the value is in the 
        invalid_invalid_company_name_check_list, contains characters that are not normally allowed.
        """
        #Creating a list of bad company to use in test
        invalid_invalid_company_name_check_list = [" ","  ","   ","    ","     ", "      ","       ","        "]
        #Calling company_name_check and passing home in the arguments
        for company in invalid_invalid_company_name_check_list:
            self.assertFalse(self.my_customer.company_name_check(company.strip()))
    def test_valid_company_name_check(self): 
        """
        Test to see if the company name is valid.
        Test ran: assertFalse.
        assertTrue - Checks to see if the value is in the valid_company_name_check_list,
        assertTrue returns true if it is.
        """
        valid_company_name_check_list = ["$Dollar Store","DollarStore","Dollar Store","Dollar Store#","Dollar Store123","a","a1","1a","dollar store","dollarstore","DOLLAR STORE"," Dollar Store","Dollar Store "," Dollar Store","1dollar3 store","6dollar1 3store2","dollar3 5store2","*dollar1 !store2","(dollar$ !store@","@dollar$ 3store2"]
        #Calling company_name_check and passing home in the arguments
        for company in valid_company_name_check_list:
            #Evaluating the company name method.
            self.assertTrue(self.my_customer.company_name_check(company))
    def test_invalid_customer_name_check(self):
        """
        Test to see if the customer name is invalid.
        Test ran: assertTrue - Checks to see that the customer name
        contains characters that are not either -, ', a space, and letters.
        """
        #Creating a list of valid names to test.
        invalid_names_list = ["!Phil","!Phil#","!Ph#il$","*phil","*phil$","*ph#il^","*PH'IL","*ph'il-","*phi- l","*'ph'il'","!- '%","1phil","1phil7","phil6","4phil'","7phil-","1ph4353il","12345434","7phil$","&$#@((*&%",""," "]
        #Looping through each name in the list.
        for name in invalid_names_list:
            #Evaluating the customer name method.
            self.assertFalse(self.my_customer.customer_name_check(name))
    def test_valid_customer_name_check(self):
        """
        Test to see if the company name is valid.
        Test ran: assertTrue - Checks to see that the customer name
        only contains - ' a space, and letters
        """
        #Creating a list of valid names to test.
        valid_names_list = ["Phil","phil","PHIL","'phil","ph il","PH'IL","phil'","phil-","-phil","'ph- il","-ph'i l","-' "]
        #Looping through each name in the list.
        for name in valid_names_list:
            #Evaluating the customer name method.
            self.assertTrue(self.my_customer.customer_name_check(name))
    def test_invalid_email(self): 
        """
        Test to see if the customer email is invalid.
        Test ran: assertFalse.
        assertFalse - Checks to see if the value is in the customer 
        email list or contains characters that are not normally allowed.
        """
        #Creating a list of bad emails to test.
        invalid_email_list= ["!mary123@mail.com","!mary12@#$3@()$#*&mail.com%","!mary123@mail.com%","mary123@mail.com#","mary123mailcom#","MARY!MAILCOM","#mary123mailcom!","mary!mailcom","mary!gmail.com","$mary123mailcom","^&^*&#!@",""," "]
        #Calling retail_price_check and passing home in the arguments
        for email in invalid_email_list:
            #Evaluating each email in the list.
            self.assertFalse(self.my_customer.email_check(email))
    def test_valid_email(self): 
        """
        Test to see if the customer email is valid.
        Test ran: assertFalse.
        assertTrue - Checks to see if the value is in the customer 
        email list, assertTrue returns true if it is.
        """
        #Creating a list of good emails to test.
        valid_email_list= ["mary123mail.com","mary123mail.com","marymail.com","a","i3@","3@3.com","a@","a.",".d","@d","marymailcom","1marymailcom4","4marymailcom","marymailcom6","marrymailcom","marymail","sally73@gmail.com","SALLY73@GMAIL.COM","4marymailr3242com3","9324759872395734","mary123@mail.com"]
        #Calling retail_price_check and passing home in the arguments
        for email in valid_email_list:
            #Evaluating each email in the list.
            self.assertTrue(self.my_customer.email_check(email))
    def test_invalid_phone_check(self): 
        """
        Test to see if the customer phone number is not valid.
        Test ran: assertFalse.
        assertFalse - Checks to see if the value is in the 
        invalid_phone_check list checks to see if it 
        contains characters that are not normally allowed.
        """
        #Creating a list of bad phone numbers to test.
        invalid_phone_check = ["212.599.6363","!2125996363","2125996363!","Tom! Petz*","##Cindy##","a2259a","aaa.bbb.cccc","&$#(&@*(&#$@&(#@*","","jkahdfjhsafkdh","&*#-#&$-#$&*"," ",'&@#($&#42343&($!#(2432&*#(@$$*',"423342432a)","f231213321","d1232(1323h","*123231231","231231213$","^231a23132","g32132123&"]
        #Calling phone_number_check and passing the number in the arguments
        for phone in invalid_phone_check:
            #Evaluating each phone number in the list.
            self.assertFalse(self.my_customer.phone_number_check(phone))
    def test_valid_phone_check(self): 
        """
        Test to see if the customer phone number is valid.
        Test ran: assertTrue.
        assertTrue - Checks to see if the value is in the 
        valid_phone_check list, assertTrue returns true if it is.
        """
        #Creating a list of good numbers
        valid_phone_check = ["212-599-6363","212-599-6363","1234567890","123-123-1234","1111111111","-1111111111-","-1112223334-","1231233212--","--1231233212","222-222-2222","7777777777"]
        #Calling phone_number_check and passing the number in the arguments
        for phone in valid_phone_check:
            #Evaluating the phone numbers
            self.assertTrue(self.my_customer.phone_number_check(phone))
    def test_invalid_state_check(self): 
        """
        Test to see if the customer state is not valid.
        Test ran: assertFalse.
        assertFalse - Checks to see if the value is in the customer 
        state list, assertFalse checks to see if it contains characters that are not normally allowed.
        """
        #Creating a list of bad state checks.
        invalid_state_list= ["M1","dahs","ASG","A","1M","11","!M","m1","A&","1m","!!","!M","M!","","  "," "," M","I "]
        #Calling retail_price_check and passing home in the arguments
        for state in invalid_state_list:
            #Evaluating each value in the list.
            self.assertFalse(self.my_customer.state_information_check(state))
    def test_valid_state_check(self): 
        """
        Test to see if the customer state is valid.
        Test ran: assertTrue.
        assertTrue - Checks to see if the value is in the customer 
        state list, assertTrue returns true if it is.
        """
        #Creating a list of good state values.
        invalid_state_list= ["MI","mi","aZ","Az","fw"]
        #Calling retail_price_check and passing home in the arguments
        for state in invalid_state_list:
            #Evaluating each value in the list.
            self.assertTrue(self.my_customer.state_information_check(state))
    def test_invalid_zip_code_check(self): 
        """
        Test to see if the customer zip code is not valid.
        Test ran: assertFalse.
        assertFalse - Checks to see if the value is in the customer 
        state list, assertFalse checks to see if it contains characters that are not normally allowed..
        """
        #Creating a list of bad zip code values to test.
        invalid_state_list= ["123m","!423d","12m3","12345678","!123","123!","12!3","123","0","12","as","!","a","wq","as2d","asfd","asfdd","@#","$@#","$#@@","j#@a","j23i","2sd@","@df4","asd1",""," "]
        #Calling retail_price_check and passing home in the arguments
        for state in invalid_state_list:
            #Evaluating each value in the list.
            self.assertFalse(self.my_customer.zip_code_check(state))
    def test_valid_zip_code_check(self): 
        """
        Test to see if the customer zip code is valid.
        Test ran: assertTrue.
        assertTrue - Checks to see if the value is in the customer 
        zip code list, assertTrue returns true if it is.
        """
        #Creating a list of good values to test.
        valid_zip_code_list= ["1234","4321","12345","1111","11111","1112","2111","2112","21112","31115","21314"]
        #Calling retail_price_check and passing home in the arguments
        for zip_code in valid_zip_code_list:
            #Evaluating each value in the list.
            self.assertTrue(self.my_customer.zip_code_check(zip_code))
