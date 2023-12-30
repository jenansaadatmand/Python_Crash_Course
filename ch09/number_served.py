# Number served: start with your program from execersize 9-1(page 162).
# Add on an attribute called number_served with a default value of 0
# Create an instance called restaurant from this class
# print the number of customers the restaurant has served, and
# then change this value and print it again
# Add a method called set_number_served() that lets you set the number of customers that have been served
# call this method with your new number and print the value again

class Restaurant:
    """A class representing or modeling a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the reastaurant"""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0   # creating an attribute called number_served with default value = 0

    def describe_restaurant(self):
        """Displays a summary of the restaurant"""
        print(f"\n{self.name} offers {self.cuisine_type} cuisine.")
        #alternatively, can use this code:
        msg = f"{self.name} serves wonderful {self.cuisine_type} curry."
        print(f"\n{msg}") 

    def open_restaurant(self):
        """Displays or simulate the retaurant is open."""
        print(f"\n{self.name} is open.")
        # alternatively can use this code:
        msg = f"{self.name} is open. Come on in!."
        print(f"\n{msg}")


    def set_number_served(self, number_served): # setting a new method
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

        
    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served
        

restaurant = Restaurant('india town', 'Indian')
restaurant2 = Restaurant('Arabic town', 'Arabic')

print(restaurant.name)
print(restaurant.cuisine_type)
print(restaurant.number_served) # accessing the number_served value
restaurant.describe_restaurant()
restaurant.open_restaurant()
print()


# changing the Attribute's value directly:
#print(f"\nCustomers served: {restaurant.number_customers_served}") # printing the number of customers the restaurant has served
#restaurant.number_served = 50  # change the number of customers the restaurant has served directly by accessing the attribute from 0 to 23
#print(f"Customers served: {restaurant.number_customers_served}") # printing the value of customers served again

# printing current number served
print(f"Number served: {restaurant.number_served}")
restaurant.number_served = 430
print(f"Number served: {restaurant.number_served}")

# changing the attribute's value via a method:

restaurant.set_number_served(1257) # calling the new function 
print(f"\nNumbers served: {restaurant.number_served}")
print()

#restaurant.set_number_served(-1) # setting a negative number
#print(f"\nNumbers served: {restaurant.number_customers_served}")

# incrementing the attribute's value

restaurant.increment_number_served(239)
print(f"\nNumber served: {restaurant.number_served}")

#restaurant.increment_number_served(-200) # incrementing with a negative value
#print(f"\nNumber served: {restaurant.number_customers_served}")