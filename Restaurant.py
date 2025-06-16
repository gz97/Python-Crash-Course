class Restaurant:
    """ 
    A class that models a restaurant
    """

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title() 
        self.cuisine_type = cuisine_type.lower()
        self.number_served = 0

    def describe_restaurant(self):
        print(f"My restaurant is called: {self.restaurant_name}.")
        print(f"My restaurant serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self, customers):
        self.number_served = customers

    def increment_number_served(self, customers_increment):
        self.number_served += customers_increment