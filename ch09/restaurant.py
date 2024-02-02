# Restaurant: Make a class called restaurant
# The __init__() for restaurant should store two attributes:
# A restaurant name and a cuisine_type
# Make a method called describe_restaurant() 

# That print these two pieces of information, and a
# Method called open_restaurant() that prints a message indicating that the restaurant is open
# Make an instance called restaurant from your class
# Print the two attributes individually, and then call both methods

class Restaurant:
    """A class representing or modelling a restaurant"""
 
    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Displays a summary of the restaurant."""
        print(f"{self.name} offer {self.cuisine_type} cusine.")
        #alternatively, can use this code:
        msg = f"{self.name} serves wonderful {self.cuisine_type} curry."
        print(f"\n{msg}") 

    def open_restaurant(self):
        """Display or Simulate the restaurant is open."""
        print(f"{self.name} is open.") 
        # Alternatively can use this code:
        msg = f"{self.name} is open. Come on in!."
        print(f"\n{msg}")

restaurant = Restaurant('india town', 'Indian')

print("Printing two attributes:")
print(restaurant.name)
print(restaurant.cuisine_type)
print("\n")

print("Calling two methods:")
restaurant.describe_restaurant() 
print("\n")
restaurant.open_restaurant()
