# Refactoring or code compartmentalization using a series of functions
# Refactor greet_user() function p_206 so its not doing many tasks
# move the code of retrieving a stored username to a separate function

import json
def get_stored_username(): # retrieving a stored username if one exist 
    """Get stored username if available.""" # docstring
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError: # if file doesn't exist, it return none
        return None 
    else: 
        return username    

def get_new_username(): # prompting for a new username if one doesn't exist
    """Prompt for a new username."""
    username = input("Waht is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user(): # we are using a function for greeting the user by name
    """Greet the user by name."""
    username = get_stored_username()
    if username: # print msg back to user if attempt to retrieve a username was successful
        print(f"Welcome back, {username}!")
    else: # if unsuccessful, prompt for new username
        username = get_new_username()
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(f)
            print(f"We'll remember you when you come back, {username}!")
    
greet_user()  # call greet_user(), that function prints an appropriate messages: it either welcomes back an existing user or greets a new user.

# greet_user() does this by calling get_stored_username(), which is responsible only for retrieving a stored username if one exists
# and greet_user() also calls get_new_username() if necessary, which is responsible only for getting a new username and storing it.
