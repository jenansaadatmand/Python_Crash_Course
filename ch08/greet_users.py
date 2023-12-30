# passing a list to a function
# list of names, numbers, dictionaries ....etc
# when you pass a list to a function, the function gets direct access to the contents of the list
# we have a list of users, we want to print  a greeting to each
# program sends a personalized greeting to each user by sends a list of names to a function called greet_users(), which greets each person in the list individually

def greet_users(names): # define the function to expect list of names, which it assigns to a parameter names
    """print a simple greeting to each user in the list."""
    for name in names: # function loops through the list it recieves 
        msg = f"Hello, {name.title()}!" 
        print(msg) # prints a greeting to each user
usernames = ['hannah', 'try', 'margot'] # define a list of users
greet_users(usernames) # pass the list usernames to the function in our call

print("\n")

# you can call the function anytime using a specific set of users
usernames_b = ['jimmy', 'jenan', 'tifany']
greet_users(usernames_b)
