# Combining storing and reading/recovering data using json in one program or file
# when someone runs remember_me.py, we want to retrieve their username from memory if possible
# start with a try block that attempts to recover the username
# If the file username.json does not exist, we'll have the except block prompt for a username and store it in username.json for next time

import json
# load the username, if the username has been stored previously.
# otherwise, prompt for the username and store it

filename = 'username.json'
try: # try to open the file username.json. if the file exists, we read the username back into memory and print a message welcoming back the user in the else block
    with open(filename) as f: 
        username = json.load(f) # load read back into memory
except FileNotFoundError: # if this is the firsttime the user runs the program, username.json does not exist, exception error is raised, handled by except block prompt user to enter their username
    username = input("What is your name?") 
    with open(filename, 'w') as f:
        json.dump(username, f) # store username and print greetings
    print(f"We'll remember you when you come back, {username}!")
else: 
    print(f"Welcome back, {username}!")
