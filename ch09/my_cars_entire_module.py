# You can also import an entire module and then access the classes you need using dot notation.
# Access classes through module_name.ClassName syntax
# Also you can import every class from a module using the following syntax:
# From module_name import * 
# This syntax is not recommended, not clear which class you are using from the module when you read it and there is a chance of overwriting exisiting or confuse names of Class and functions in your program 

import car   # Import the entire Module and use dot notation to access classes

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())



