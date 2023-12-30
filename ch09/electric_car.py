# inhertance: parent and child class
# writing a new class (child) based on an existing class (parent)
# need to call the __init__() method from the parent class, to initialize any attributes that were defined in the parent ___init__() method and make them available in the child class
# model an electric car, a specific kind of car, based on car class, p162
# Then we'll only have to write code for the attributes and behavior specific to electric cars
# simple version of ElectricCar class, which does everything the car class does

class Car:  # start with defining the parent class, must appear in the current .py file when making a child class
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
        
class ElectricCar(Car): # define child class, the name of the parent class must be included in parentheses in the definition of a child class
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year): # __init__() takes the information required to make a Car instance
        """
        Initialize attributes of the parent class.
        Then initializa attributes specific to an electric car.
        """
        super().__init__(make, model, year) # super() function allows to call a method from the parent class, tells python to call the __init__() method from Car, which gives an ElectricCar instance all the attributes defined in that method. Superclass (Parent class) and subclass (child class) convension
        self.battery_size = 75  # add a new attribute, set it initial value to 75. will be associated will all instances created from ElectricCar but will not be associated with any instance from Car parent class

    def describe_battery(self): # add a new method
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")
#        print("This car has a " + str(self.battery_size) + "-kWh battery.") # alternatively, can use this syntax

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")


# aside from the __init__() method there are no attrbutes that are particulr to ElectricCar child class, we just made sure that the elecrtic car has the appropriate Car behavior

my_tesla = ElectricCar('tesla', 'model s', 2019) # test the inheritance is working, by trying to create an electric car with the same kind of information we'd provide when making a regular car. make instance ElectricCar and assing it to my_tesla. This line calls the __init__() method defined in ElectricCar child class, which in trun tells python to call the __init__() method defined in the parent class Car.
print(my_tesla.get_descriptive_name())


# Defining Attributes and methods for the child class: to differentiate it from parent class
# let's add an attribute specific to electric cars, a batter and a method to report on this attribute.
# Store the batter size and write a method that preints a description of the battery
# corresponding code is on lines 49, 51, 52, and 53

my_tesla.describe_battery() 


# if you ever get this error: AttributeError: 'ElectricCar' object has no attribute 'describe_battery'
# solution is look at def function indentation at line 51. unindent the def of function

# Overriding methods from the parent class despite inheritance
# you can override any method from parent class that doesn't fit what you're trying to model with the child class
# To do this, you define a method in the child class with the same name as the method you want to override in the parent class, python will disregard the parent class method and only pay attention to the method you defined in the child class
# eg. The class car had a method called fill_gass_tank(), this method meaningless for all electric vehicles
# so you want to override this method, code in line 60 overrides line 40

my_tesla.fill_gas_tank()
print()


# Instances as Attributes: 
# see code in instances_attributes_electric_car.py
# when modeling somthing from real world in code, you might find that you're adding more and more detail to a classs, a growing list of attributes and methods and you files becomes lengthy
# In these situation, you might recognize that part of one class can be written as a separate class
# break large class into smaller classes that work together
# eg. if we continue adding detail to ElectricCar classs, we might add many attributes and methods specific to the car's battery.
# when we see this happening we stop and move those attributes and methods to a seprarate class called battery.
# Then we use battery instance as an attribute in the ElectricCar class:






