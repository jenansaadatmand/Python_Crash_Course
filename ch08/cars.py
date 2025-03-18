# Cars: write a function that stores information about a car in a dictionary
# The function should always receive a manufacturer and a model name
# It should then accept an arbitrary number of keyword arguments
# Call the function with the required information and two other name-value pairs, 
# Such as a color or an optional feature
# Your function should work for a call like this one:
# Car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that's returned to make sure all the information was 
# Stored correctly


def make_car(manufacturer, model, **car_info): # Can use **car_info instead
    """Make a dictionary representing a car."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info 

car = make_car('subaru', 'outback', color='black', tow_package=True) 
print(car)

print("\n")

# Solution 2: 

def make_car(manufacturer, model, **kwargs): # can use **car_info instead
    """Stores information about a car in a dictionary."""
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs 

car = make_car('subaru', 'outback', color='black', tow_package=True) 
print(car)

print("\n")

# Solution 3:

def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }
    for option, value in options.items():
        car_dict[option] = value
    return car_dict

my_out_back = make_car('sabaru', 'outback', color='blue', tow_package=True) # True is a default value. convention: no spaces should before or after the = sign.
print(my_out_back)

print("\n")

my_old_accord = make_car('honda', 'accord', year=1991, color='white', headlights = 'popup')
print(my_old_accord)
