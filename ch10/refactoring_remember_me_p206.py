# Refactoring or code compartmentalization using a series of functions
# Refactor greet_user() function p_206 so its not doing many tasks
# Move the code of retrieving a stored username to a separate function

import json
def get_stored_username(): # Retrieving a stored username if one exists 
    """Get stored username if available.""" # docstring
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError: # If the file doesn't exist, it returns none
        return None 
    else: 
        return username    

def get_new_username(): # Prompting for a new username if one doesn't exist
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user(): # We are using a function for greeting the user by name
    """Greet the user by name."""
    username = get_stored_username()
    if username: # Print msg back to user if attempt to retrieve a username was successful
        print(f"Welcome back, {username}!")
    else: # If unsuccessful, prompt for new username
        username = get_new_username()
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(f)
            print(f"We'll remember you when you come back, {username}!")
    
greet_user()  # Call greet_user(), that function prints an appropriate message: it either welcomes back an existing user or greets a new user.

# greet_user() does this by calling get_stored_username(), which is responsible only for retrieving a stored username if one exists
# And greet_user() also calls get_new_username() if necessary, which is responsible only for getting a new username and storing it.
