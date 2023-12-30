# Saving and Reading User-Generated Data using json
# prompt user for their name the first time they run the program and then remember their name when they run the program again 
# start by storing the username

import json
username = input("What is your name? ") # prompt for a username to store in the username variable
filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f) # store the username in a file
    print(f"We'll remember you when you come back, {username}!") # msg informing the user we stored their username 
    