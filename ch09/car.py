# Creating a module for Car class, storing a class or multiple classes in a module

"""A set of classes used to represent gas and electri car."""  # Module-level docstring briefly describes the content of this module

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year): # No need to include the default value parameter odometer_reading here
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # attribute defined and assigned a default value of 0 without passing it as a parameter above in __init__() method

    def get_descriptive_name(self):    
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self): # new method is defined
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage): # method updates the self.odometer_reading attribute's value
        """
        Set the odometer reading to the given value. 
        reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading: # update_odometer() checks the new reading makes sense before modifying the attribute, if the new mileage is greater than or equal to the existing mileage, self.odometer_reading, you can update the odometer reading tot he new mileage
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!") # if the new mileage is less than existing mileage, you'll get a warning that you can't roll back an odometer

    def increment_odometer(self, miles):
        """
        Add the given amount to the odometer reading.
        reject the negative increments if attempts to roll back the odometer.
        """
        if miles >= 0:
            self.odometer_reading += miles

        else: 
            print("You can't roll back an odometer!")


class Battery:  # define a new class Battery that doesn't inherit from any other class
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75): # optional parameter sets the battery's size to 75 if no value is provided
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self): # this method has been moved from ElectricCar class to Battery class
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self): # new method performs simple analysis 
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75: # If the battery capacity is 75 kWh, get range() sets the range to 260 miles, it then reports this value
            range = 260
        elif self.battery_size == 100: # if the capacity is 100 kWh, it sets the range to 315 miles, it then reports this value
            range = 315

        print(f"This car can go about {range} miles on a full charge.")   # outcome tells us the range of the car based on its battery size
        

    def upgrade_battery(self):
        """Upgrade the battery if possible. Checks battery size and sets capacity to 100"""
        if self.battery_size != 100:
            self.battery_size=100    
            print("Upgraded the battery to 100 kwh.")
        else:
            print("The battery is already upgraded")    


class ElectricCar(Car): # define child class, the name of the parent class must be included in parentheses in the definition of a child class
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year): # __init__() takes the information required to make a Car instance
        """
        Initialize attributes of the parent class.
        Then initializa attributes specific to an electric car.
        """
        super().__init__(make, model, year) # inheritance, super().__init__() function allows to call a method from the parent class, tells python to call the __init__() method from Car, which gives an ElectricCar instance all the attributes defined in that method. Superclass (Parent class) and subclass (child class) convension. no : at the end
        self.battery = Battery()  # add a new attribute called self.battery, this line tells Python to create a new instance of Battery (with default size of 75, because we're not specifying a value) and assign that instance to the attribute self.battery. eg of an instance from another class used as an attribute
        # attribute = instance # assign that instance Battery() to the attribute self.battery. This happens every time the __init__() method is called, any ElectricCar instance will now have a Battery instance created automatically
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")



