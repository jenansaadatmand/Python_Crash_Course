# Battery upgrade: Use the final version of electric_car.py from this section
# Add a method to the battery class called upgrade_battery().
# This method should check the battery size and set the capacity to 100 if it isn't already.
# Make an electric car with a default battery size
# Call get_range() once, and then 
# Call get_range() a second time after upgrading the battery.
# You should see an increase in the car's range


class Car:  # Start with defining the parent class, must appear in the current .py file when making a child class
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
        
class Battery:  # Define a new class Battery that does't inherit from any other classs
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75): # Optional parameter sets the battery's size to 75 if no value is provided
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self): # This method has been moved from ElectricCar class to Battery class
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self): # new method performs simple analysis 
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75: # If the battery capacity is 75 kWh, get range() sets the range to 260 miles, it then reports this value
            range = 260
        elif self.battery_size == 100: # If the capacity is 100 kWh, it sets the range to 315 miles, it then reports this value
            range = 315

        message = f"This car can go approximately {range}"   # outcome tells us the range of the car based on its battery size
        message += "miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Upgrade the battery if possible. Checks battery size and sets capacity to 100"""
        if self.battery_size != 100:
            self.battery_size=100    
            print("Upgraded the battery to 100 kwh.")
        else:
            print("The battery is already upgraded")    


class ElectricCar(Car): # define child class, the name of the parent class must be included in parentheses in the definition of a child class
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year): # __init__() takes the information required to make a Car instance
        """
        Initialize attributes of the parent class.
        Then initializa attributes specific to an electric car.
        """
        super().__init__(make, model, year) # inheritance, super().__init__() function allows to call a method from the parent class, tells python to call the __init__() method from Car, which gives an ElectricCar instance all the attributes defined in that method. Superclass (Parent class) and subclass (child class) convension. no : at the end
        self.battery = Battery()  # add a new attribute called self.battery, this line tells python to create a new instance of Battery (with default size of 75, because we're not specifying a value) and assing that instance to the attribute self.battery. eg of an instance from another class used as an attribute
        # attribute = instance # assign that instance Battery() to the attribute self.battery. This happens everytime the __init__() method is called, any ElectricCar instance will now have a Battery instance created automatically
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")


print("Make an electric car, and check the range:")

my_tesla = ElectricCar('tesla', 'model s', 2019) #creating an ElectricCar instance and assign it to variable my_tesla, test the inheritance is working, by trying to create an electric car with the same kind of information we'd provide when making a regular car. make instance ElectricCar and assing it to my_tesla. This line calls the __init__() method defined in ElectricCar child class, which in trun tells python to call the __init__() method defined in the parent class Car.
print(my_tesla.get_descriptive_name())
print()

# Describing the battery of an electricCar instance by working through the car's battery attribute
my_tesla.battery.describe_battery() # create an electric car and assign it to the variable my_tesla. When we want to describe the battery, we need to work through the car's battery attribute
print()

my_tesla.battery.get_range() # when we want to use this method, we again call it through the car's battery attribute 
print()

print("\nUpgrade the batter, and check the range again:")
print()

my_tesla.battery.upgrade_battery()
print()

my_tesla.battery.get_range()



