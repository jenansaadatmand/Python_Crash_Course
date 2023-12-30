# Importing multiple Classes from a Module
# If we want to make a regular car and an electric car (two instances) in the same file, import both classes Car and ElectricCar

from car import Car, ElectricCar  # separate each class with a comma

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())


