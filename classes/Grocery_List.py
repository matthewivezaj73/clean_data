class GroceryList:
    """
    Creating a class that represents a grocery list.
    """
    def __init__(self,grocery_name,sales_price,price_paid,grocery_quantity):
        """
        Initializing the following attributes:
        - grocery_name
        - sales_price
        - price_paid
        - grocery_quantity
        """
        self.grocery_name = grocery_name
        self.sales_price = sales_price
        self.price_paid = price_paid
        self.grocery_quantity = grocery_quantity
    def add_item(self,item_name):
        """
        Created a method that represents the act of adding an item to the list
        """
        #Creating a list of groceries available.
        my_groceries = ['Gallon of milk', 'Carton of eggs', 'Cheese block', 'Yogurt', 'Apples', 'Bananas', 'Carrots', 'Tomatoes', 'Potatoes', 'Broccoli', 'Meat', 
        'Chicken breast', 'Fresh fish', 'frozen fish', 'Grains', 'Loaf of bread', 'Dry pasta', 'Brown rice', 'Couscous', 'Tomato sauce', 'Peanut butter', 'Granola bars', 
        'Extra protein', 'Nuts', 'Dried beans', 'canned beans']
        #Checking to see if the grocery entered is available. If so, prints a message and returns True.
        if item_name in my_groceries:
            print(f"{item_name} is available!")
            return True
        #If the grocery is not found, prints a message and returns false.
        else:
            print(f"{item_name} is not in the list of groceries! Please search for something else!")
            return False
    def check_price(self,item_name):
        """
        Creating a method that will check the price of a grocery entered.
        """
        #Creating a dictionary of items and their prices.
        my_prices = {'Gallon of milk':1.99, 'Carton of eggs': 2.88, 'Cheese block': 3.00, 'Yogurt': .99, 'Apples': .89, 
        'Bananas':1.21, 'Carrots':1.09, 'Tomatoes':3.99, 'Potatoes':2.89, 'Broccoli':2.33, 'Meat':3.76, 'Chicken breast':4.32, 'Fresh fish':2.99, 'frozen fish':2.95, 'Grains':1.88, 
        'Loaf of bread':1.32, 'Dry pasta':1.00, 'Brown rice':3.20, 'Couscous':2.95, 'Tomato sauce': 1.99, 'Peanut butter':2.00, 'Granola bars':1.44,'Extra protein':3.99, 'Nuts':2.50, 'Dried beans':3.00, 'canned beans':1.99}
        if item_name in my_prices.keys():
            print(f"the price for {item_name} is {item_name.value()}")
            return True
        else:
            print(f"{item_name} is not an item, please try again")
            return False
    def remove_item(self,item_name):
        """
        Created a method that represents the act of removing an item from the list.
        """
        if item_name in my_groceries.keys()