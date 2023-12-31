# Saving and Reading User-Generated Data using json
# Prompt user for their name the first time they run the program and then remember their name when they run the program again 
# Start by storing the username

import json
username = input("What is your name? ") # Prompt for a username to store in the username variable
filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f) # Store the username in a file
    print(f"We'll remember you when you come back, {username}!") # msg informing the user we stored their username 
    
