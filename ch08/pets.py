# function tells us what kind of animal each pet is and the pet's name
# positional argument page 132 in book 
def describe_pet(animal_type, pet_name): # parameters included
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')  # pass postional argument when recalling a function


# multiple function calls, calling a function multiple times 
# add another positional argument to the called function for a different pet
# make sure the order of the arguments in your function call matches the order of the parameters in the function’s definition
describe_pet('dog', 'willie')
describe_pet('harry', 'hamster')  # order of positional arguments matter
print()
print()
# A keyword argument is a name-value pair that you pass to a function.


# rewriting the program using a keyword argument
describe_pet(animal_type = 'hamster', pet_name = 'harry')
print()
describe_pet(pet_name='harry', animal_type='hamster')
print()
# default values for parameters, exclude the argument value in the function call
# example most function calls used to describe an animal_type to 'dog'

def describe_pet(pet_name, animal_type = 'dog'):    # setting a default value when defining the function
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')
print()


# To describe an animal other than a dog, you could use a function call
describe_pet(pet_name='harry', animal_type = 'hamster')
print()

# various styles to call the function using positional arguments, keyworords arguments, and default values combination
# a dog named willie
describe_pet('willie')
describe_pet(pet_name='willie')
# a hamster nammed harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
print()



