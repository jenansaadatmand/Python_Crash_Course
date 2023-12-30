# Three Restaurants: start with your calss from exercise 9-1.
# Create three different instances from the class, and 
# call describe_restaurant() for each instance

class Restaurant:
    """A class representing or modeling a Restaurant."""
 
    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Displays a summary of the restaurant."""
        print(f"{self.name} offers {self.cuisine_type} cuisine.")
        # alternatively you can use:
        msg = (f"{self.name} serves a wonderful {self.cuisine_type} cuisine.")
        print(f"\n{msg}")

    def open_restaurant(self):
        """Displays or simulate the restaurant is open."""
        print(f"{self.name} is open.")
        # alternatievely you can use this code:
        msg = f"{self.name} is open. Come on in."
        print(f"\n{msg}")

india_town = Restaurant('india town', 'Indian')
seaside = Restaurant('seaside', 'Seafood')
italiano = Restaurant('italiano', 'Pizza')

# using describe_restaurant() for each instance
india_town.describe_restaurant()
seaside.describe_restaurant()
italiano.describe_restaurant()



