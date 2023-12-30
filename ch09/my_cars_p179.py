# Importing a module into a module, when one module depends on a class in another module

from carp178 import Car
from electric_car_p178 import ElectricCar as EC   # using aliases instead of typing the name of all the class each time, use shorter alias 'EC'

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
