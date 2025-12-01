# Ice Cream Stand: An ice cream stand is a specific kind of restaurant
# Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Excersize 9-4 (page 167)
# Either version of the class will work; just pick the one you like better
# Add an attribute called flavors that stores a list of ice cream flavors
# Write a method that displays these flavors
# Create an instance of IceCreamStand, and call this method

class Restaurant: # Excersize 9-1 (page 162)
    """A class representing or modelling a restaurant"""

    
    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Displays a summary of the restaurant."""
        print(f"{self.name} offer {self.cuisine_type}.")
        #Alternatively, can use this code:
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
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
print()

print("Calling two methods:")
restaurant.describe_restaurant() 
print()
restaurant.open_restaurant()
print("\n\n\n")


class IceCreamStand(Restaurant): # Inheretance
    """Represent an IceCreamStand."""

    def __init__(self, name, cuisine_type='ice_cream'):  # You add a default parameter for cuisine_type
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to Ice Cream Stand child class.
        """
        super().__init__(name, cuisine_type)
        self.flavors = ['strawberries', 'blueberries', 'raspberries'] # Add an attribute called flavors that stores a list of ice creams flavors, set an empty list to contain the flavors ordered
    
    def show_flavors(self):  # A method that displays these flavors
        """Displays available ice cream flavors."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors: # A for loop to loop through the list flavors
            print(f"- {flavor.title()}")

ice_cream = IceCreamStand('Gelato', 'ice cream')  # An ice_cream_stand instance is created
#ice_cream.flavors = ['strawberries', 'blueberries', 'raspberries'] # creating a list of ice cream flavors, defining the list flavors.  Alternatively, we can add the flavors inside line 53 instead of an empty list

ice_cream.describe_restaurant()  # Calling the method that describes the restaurant information
print()

ice_cream.show_flavors() # Calling the method that describes these flavors
