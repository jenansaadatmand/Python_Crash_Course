# Program that greets a user whose name has already been stored

import json
filename = 'username.json'
with open(filename) as f:
    greetings = json.load(f) # to read the stored information in username.json, assign to variable
    print(f"Welcome back, {greetings.title()}!") # Print recovered username, we welcome back the user once logged in again
    
