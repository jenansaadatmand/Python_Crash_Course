# Refactoring: breaking up code into a series of functions. improving the code by breaking it up into a series of functions that have specific jobs
# Refactoring makes code cleaner, easier to understand and to extend
# Let's refactor remember_me.py on p206 by moving the bulk of its logic into one or more functions
# Focus of remember_me.py is on greeting the user, 
# so let's move all of our existing code into a function called greet_user()

import json
def greet_user(): # we are using a function now, greeting the user and retrieving a stored username if one exist and prompting for a new username if one doesn't exist
    """Greet the user by name."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ") 
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")

greet_user()

# The UnboundLocalError: local variable referenced before assignment error is raised when you try to assign a value to a local variable before it has been declared. You can solve this error by ensuring that a local variable is declared before you assign it a value.
# I used or referenced username in line 20 in else block but I did not declare it in line 13 as username variable = json.load(f)
