# storing your functions in modules
# functions separate blocks of code from your main program.
# using descriptive function name makes your program easier to follow
# storing your function in a seprate file called module and then importing that module into your main program.
# an import statement tells python to make the code in a module available in the currently running program file.
# storing function in module allows you to use your function in different programs
# also allows you to hide the details of your function code and focus on higher logic level programs
# also you can share function modules with others withour having to share entire program.
# knowing how to import functions also allows you to use libraries of functions that other programmers have written
# there are several ways to import a module as follows: 
# 1. importing entire module, 
#import module 
#import module
#module_name.function_name() # call the function using dot notation
# 2. importing specific functions, 
#from module_name import function_name
# function_name() to call the function
# 3. using as to give a function an Alias,
#from module_name import function_name as fn 
# fn() to call the function
# 4. using as to give a module an Alias, 
#import module_name as mn
# mn.function_name() # to call the function
# 5. and importing every/all functions in a module. not recommended method because python can confuse or overwrite other functions with the same name in your program
#from module_name import * 
#function_name() to call the function




#1. Importing an Entire modules using the dot notation
# first create a module, then import it to your program file

# A module is a file ending in .py that contains the code you want to import into your program
# let's make a module that contains the function make_pizza(), call it pizza_mod.py
# now we make a separate file called making_pizzas.py in the same directory as pizza_mod.py
