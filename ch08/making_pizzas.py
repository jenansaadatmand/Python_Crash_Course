# This program imports the pizza_mod.py module and makes two calls to make_pizza() 
# Any function that was defined in the module will now be available to be used in this program
# Step 1: creating the module

# Step 2: importing the modlue, import followed by name of module, import statement makes every function in the module available for this program, i.e: entire module content, each function

import pizza_mod  # tells python to open the file pizza_mod.py and copy all the functions from it into this program. Notice you leave out the .py in the file name

# Step 3: calling the function from the imported module. enter name of module, followed by name of function, separated by a dot, syntax: module_name.function_name(arguments)

pizza_mod.make_pizza(16, 'pepperoni')
pizza_mod.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



# The outcome of this program is similar to the outcome of the pizza.py program that did not import a module
