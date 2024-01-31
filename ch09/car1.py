# Working with classes and instances, p162
# Modifying attributes associated with instances in a class
# You can modify attributes of an instance directly or write methods that update attributes in specific ways
# New class representing car. Car will store information about the kind of the car and it will have a method that summarizes this information


#class Car:
#    """A simple attempt to represent a car."""

#    def __init__(self, make, model, year): # --init--() takes the parameters and assigns them to the attributes that will be associated with instances made from this class
#        """Initialize attributes to describe a car."""
#        self.make = make
#        self.model = model
#        self.year = year


#    def get_descriptive_name(self): # Define a method that puts all the parameters into one string neatly describing the car. instead of printing each attribute's value individually
#        """Return a neatly formatted descriptive name."""
#        long_name = f"{self.year} {self.make} {self.model}" # To work with attribute's values, we use self.parameter
#        return long_name.title()

#my_new_car = Car('audi', 'a4', 2019) # Making a new car instance from Car class and assigning it to the variable my_new_car, we give it attributes, these attributes will be associated with parameters in the __init__() method
#print(my_new_car.get_descriptive_name()) # Printing the calling of the get_descriptive_name() method (because it only returns a value and does not print)to show what kind of car we have.

# Adding an attribute that changes over time
# We will add an attribute that stores the car's overall mileage
# Setting a Default Value for an Attribute
# When an instance is created, attributes can be defined without being passed in as parameters
# These attributes can be defined in the __init__() method, where they are assigned a default value.
# Let's add an attribute called odometer_reading that always starts with a value of 0
# We'll also add a method read_odometer() that help us read each car's odometer

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year): # No need to include the default value parameter odometer_reading here
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Attribute defined and assigned a default value of 0 without passing it as a parameter above in __init__() method

    def get_descriptive_name(self):    
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self): # new method is defined
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
#    def update_odometer(self, mileage): # Method takes in a mileage value and assigns it to self.odometer_reading
#        """Set the odometer reading to the given value."""
#        self.odometer_reading = mileage


    def update_odometer(self, mileage): # method updates the self.odometer_reading attribute's value
        """
        Set the odometer reading to the given value. 
        reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading: # Update_odometer() checks the new reading makes sense before modifying the attribute, if the new mileage is greater than or equal to the existing mileage, self.odometer_reading, you can update the odometer reading to the new mileage
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!") # If the new mileage is less than the existing mileage, you'll get a warning that you can't roll back an odometer

#    def increment_odometer(self, miles): # Method takes in a number of miles, and adds this value to self.odometer_reading
#        """Add the given amount to the odometer reading."""
#        self.odometer_reading += miles 
    
    def increment_odometer(self, miles):
        """
        Add the given amount to the odometer reading.
        reject the negative increments if attempts to roll back the odometer.
        """
        if miles >= 0:
            self.odometer_reading += miles

        else: 
            print("You can't roll back an odometer!")


my_new_car = Car('audi', 'a4', 2019)  # We cannot add odometer attribute here, it starts at 0
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer() 

# Many cars are sold with exactly 0 miles on the odometer, so we need a way to change the value of this attribute
# Modifying an attribute's value directly
# You can change an attribute's value in three ways:
# 1. By changing the value directly through an instance, 
# 2. Set the value through a method, the method will update it internally
# 3. or increment the value (add a certain amount to it) through a method

# 1. Modifying an attribute value by accessing it directly through an instance:
# Let's set the odometer reading to 23 directly

my_new_car.odometer_reading = 23 # use dot notation to access the car's odometer attribute and set its value to 23. tells python to take the instance my_new_car, find the attribute odometer associated with it and set the value of that attribute to 23
my_new_car.read_odometer()
print()

# You can do the same for other defined attributes not just the default value
#my_new_car.make = 'bmw'
#print(my_new_car.get_descriptive_name())
#print("\n")

# 2. Modifying an attribute's value through a method. by writing a method that updates the value for you
# Methods that update certain attributes for you are very helpful, instead of accessing it directly, you pass a new value to a method that will handle the updating internally

# Creating a method called update_odometer()

# This code works with lines 52, 53, and 54 being uncommented

my_new_car.update_odometer(23)  # call the method and pass 23 as an argument(corresponding the mileage parameter in the method definition)
my_new_car.read_odometer() # read_odometer() prints the reading
print()

# 2. Continue modifying attribute value with a method
# Let's extend the method update_odometer() to do additional work every time the odometer reading is modified as a check for security measure
# Uncomment code lines 57, to 65, for the below code to work, we will add a little logic to make sure no one tires to roll back the odometer reading:

my_new_car.update_odometer(8) # outcome, you cannot roll back an odometer
my_new_car.read_odometer()
print()

#3. Incrementing an attribute's value (add a certain amount to it) through a method
# Sometimes we want to increment an attribute's value rather than setting an attribute's entirely new value
# We buy a used car and put 100 miles on it between the time we buy it and the time we register it
# Uncomment method on lines 67-69, a method that allows us to pass this incremental amount and add that value to the odometer reading



my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500) # Create a used car variable that holds the instance within the class, we set its odometer to 23,500 by calling update_odometer() and passing 23,500
my_used_car.read_odometer()

my_used_car.increment_odometer(100)   # Call increment_odometer() and pass it 100 to add the 100 miles that we drove between buying the car and registering it 
my_used_car.read_odometer() #Ooutcome is 23,600
print()

# You can easily modify this increment_odometer() method to reject negative increments so no one uses this function to roll back an odometer. (checks as security measure)

# Method is on lines  

my_used_car.increment_odometer(-1)  # Because of the previous addition on line 138, the odometer currently is set on 23,600
my_used_car.read_odometer() # Negative number can't set back the odometer



