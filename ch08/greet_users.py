# Passing a list to a function
# List of names, numbers, dictionaries ....etc
# When you pass a list to a function, the function gets direct access to the contents of the list
# We have a list of users, and we want to print  a greeting to each
# The program sends a personalized greeting to each user by sending a list of names to a function called greet_users(), which greets each person in the list individually

def greet_users(names): # Define the function to expect a list of names, which it assigns to a parameter names
    """print a simple greeting to each user in the list."""
    for name in names: # Function loops through the list it receives 
        msg = f"Hello, {name.title()}!" 
        print(msg) # prints a greeting to each user
usernames = ['hannah', 'try', 'margot'] # Define a list of users
greet_users(usernames) # Pass the list of usernames to the function in our call

print("\n")

# You can call the function anytime using a specific set of users
usernames_b = ['jimmy', 'jenan', 'tifany']
greet_users(usernames_b)
