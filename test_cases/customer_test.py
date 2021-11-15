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
        removeitems = ["Waterford'","Water'ford","\'Waterford","water\'ford","waterford'","Shelby '","' Shelby"," shelby","shelby","shelby township","utic","Shelby Township","Shelby'Township","'Shelby'Township'","ShelbyTownship","shelbytownship","SHELBY","SHELBY "," SHELBY"," SHELBY ","shelby "," shelby"," shelby "," Shelby","Shelby "," Shelby "]
        #Checkings for each string in the list.
        for gprice in removeitems:
            #Evaluating each string.
            self.assertTrue(self.Grocery_List.remove_item(gprice)) 
    def test_remove_item_check(self):
        """
        """
        #Creating a list of bad company to use in test
        removeitems = [" ","  ","   ","    ","     ", "      ","       ","        "]
        #Calling company_name_check and passing home in the arguments
        for ritem in removeitems:
            self.assertFalse(self.Grocery_List.remove_item(ritem.strip()))
