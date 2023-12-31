# Defining a function called greet_user that prints a greetings
# Page 130 in book
def greet_user():   # Function definition, parenthesis is empty which holds what kind of information is needed for the function to do its work
# Body of function
    """Display a simple greeting.""" # docstring describes what the function does, enclosed in tripple quotes, used by python to generate documentation for the function in the program
    print("Hello!")     # Actual code in the body of the function, this function has only one job 
# Call the function for python to excute it:
greet_user() # you can add any necessary information in the parenthesis if required
print()

# Passing information to a function
# Modifying the previous function:
# Function greet_user() can tell the user Hello! and also greet them by name.
# The variable username in the definition of greet_user() is an example of a parameter, a piece of information the function needs to do its job.
# An argument is a piece of information that’s passed from a function call to a function.
def greet_user(username): # function accepts any value as username you specify, function requires a value for the variable username which is a parameter
    """Display a simple greeting."""
    print(f"Hello, {username.title()}")
greet_user('jesse') # passing information to the function in order to call it, The value 'jesse' in greet_user('jesse') is an argument.
greet_user('jimmy')
greet_user(username='toto')
