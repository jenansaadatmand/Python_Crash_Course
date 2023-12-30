# defining a function called greet_user that prints a greetings
# page 130 in book
def greet_user():   # function definition, parenthesis is empty which holds what kind of information needed for the function to do its work
# body of function
    """Display a simple greeting.""" # docstring decribes what the function does, enclosed in tripple quotes, used by python to generate documentation for the function in the program
    print("Hello!")     # actual code in the body of the function, this function has only one job 
# call the function for python to excute it:
greet_user() # you can add any necessary information in the parenthesis if required
print()

# Passing information to a function
# modifying the previous function:
# function greet_user() can tell the user Hello! and also greet them by name.
# The variable username in the definition of greet_user() is an example of a parameter, a piece of information the function needs to do its job.
# An argument is a piece of information that’s passed from a function call to a function.
def greet_user(username): # function accepts any value as username you specify, function requires a value for the variable username which is a parameter
    """Display a simple greeting."""
    print(f"Hello, {username.title()}")
greet_user('jesse') # passing information to the function in order to call it, The value 'jesse' in greet_user('jesse') is an argument.
greet_user('jimmy')
greet_user(username='toto')
