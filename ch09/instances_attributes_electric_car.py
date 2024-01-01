# Inhertance: parent and child class
# Writing a new class (child) based on an existing class (parent)
# Need to call the __init__() method from the parent class, to initialize any attributes that were defined in the parent ___init__() method and make them available in the child class
# Model an electric car, a specific kind of car, based on car class, p162
# Then we'll only have to write code for the attributes and behavior specific to electric cars
# Simple version of ElectricCar class, which does everything the car class does

class Car:  # Start with defining the parent class, which must appear in the current .py file when making a child class
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()  

    def read_odometer(self):
        """Prints a statement showing the cars mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer!.")

    def increment_odometer(self, miles):
        if miles >= odometer_reading:
            self.odometer_reading += miles
        else:
            print("You cannot roll back an odometer!.")

    def fill_gas_tank(self):
        """Cars need gas in tanks."""
        print("This car need gas in tank!")
        
class Battery:  # Define a new class Battery that doesn't inherit from any other class
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75): # Optional parameter sets the battery's size to 75 if no value is provided
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self): # This method has been moved from ElectricCar class to Battery class
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self): # New method performs simple analysis 
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75: # If the battery capacity is 75 kWh, get range() sets the range to 260 miles, it then reports this value
            range = 260
        elif self.battery_size == 100: # If the capacity is 100 kWh, it sets the range to 315 miles, it then reports this value
            range = 315

        print(f"This car can go about {range} miles on a full charge.")    # outcome tells us the range of the car based on its battery size


class ElectricCar(Car): # define child class, the name of the parent class must be included in parentheses in the definition of a child class
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year): # __init__() takes the information required to make a Car instance
        """
        Initialize attributes of the parent class.
        Then initializa attributes specific to an electric car.
        """
        super().__init__(make, model, year) # inheritance, super().__init__() function allows to call a method from the parent class, tells Python to call the __init__() method from Car, which gives an ElectricCar instance all the attributes defined in that method. Superclass (Parent class) and subclass (child class) convension. no : at the end
        self.battery = Battery()  # add a new attribute called self.battery, this line tells Python to create a new instance of Battery (with default size of 75, because we're not specifying a value) and assign that instance to the attribute self.battery. eg of an instance from another class used as an attribute
        # attribute = instance # assign that instance Battery() to the attribute self.battery. This happens everytime the __init__() method is called, any ElectricCar instance will now have a Battery instance created automatically
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")


# Aside from the __init__() method there are no attributes that are particular to ElectricCar child class, we just made sure that the elecrtic car has the appropriate Car behavior

my_tesla = ElectricCar('tesla', 'model s', 2019) #creating an ElectricCar instance and assigning it to variable my_tesla, test the inheritance is working, by trying to create an electric car with the same kind of information we'd provide when making a regular car. make an instance ElectricCar and assign it to my_tesla. This line calls the __init__() method defined in ElectricCar child class, which in trun tells Python to call the __init__() method defined in the parent class Car.
print(my_tesla.get_descriptive_name())
print()

# Instances as Attributes: defining battery class lines 44-53 and using instance as attributes line 65, 112
# when modeling something from real world in code, you might find that you're adding more and more detail to a classs, a growing list of attributes and methods and you files become lengthy
# In these situations, you might recognize that part of one class can be written as a separate class
# break large class into smaller classes that work together
# eg. if we continue adding detail to ElectricCar classs, we might add many attributes and methods specific to the car's battery.
# when we see this happening we stop and move those attributes and methods to a seprarate class called battery.
# Then we use battery instance as an attribute in the ElectricCar class:

# describing the battery of an electricCar instance by working through the car's battery attribute
my_tesla.battery.describe_battery() # Create an electric car and assign it to the variable my_tesla. When we want to describe the battery, we need to work through the car's battery attribute
print()

# let's add another method to a Battery that reports the range of the car based on the battery size:
# see code line 55-62 and line 103

my_tesla.battery.get_range() # When we want to use this method, we again call it through the car's battery attribute 




