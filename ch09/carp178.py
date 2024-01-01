"""A class used to represent a car."""  # Module-level docstring briefly describes the content of this module

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year): # no need to include the default value parameter odometer_reading here
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Attribute defined and assigned a default value of 0 without passing it as a parameter above in __init__() method

    def get_descriptive_name(self):    
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self): # New method is defined
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage): # Method updates the self.odometer_reading attribute's value
        """
        Set the odometer reading to the given value. 
        reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading: # Update_odometer() checks the new reading makes sense before modifying the attribute, if the new mileage is greater than or equal to the existing mileage, self.odometer_reading, you can update the odometer reading to the new mileage
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!") # If the new mileage is less than existing mileage, you'll get a warning that you can't roll back an odometer

    def increment_odometer(self, miles):
        """
        Add the given amount to the odometer reading.
        reject the negative increments if attempts to roll back the odometer.
        """
        if miles >= 0:
            self.odometer_reading += miles

        else: 
            print("You can't roll back an odometer!")

