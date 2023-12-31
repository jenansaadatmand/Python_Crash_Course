# Nesting a dictionary inside a dictionary
# Several users for a website, each with unique usernames
# Use usernames as keys in a dictionary and store user information in dictionary as a value
# Store three pieces of information about each user:
# Username, last name and location
# Access this information by looping through the usernames and the dictionary associated with each username


# Define a dictionary called users with two keys: one each for the usernames 'aeinstein' and 'mcurie'.
# Value associated with each key is a dictionary that includes each user’s first name, last name, and location
users = {
        'aeinstein':{
                    'first':'albert',
                    'last': 'aeinstein',
                    'location': 'princeton'
                    },
        'mcurie':{
            'first': 'marie',
            'last' : 'curie',
            'location': 'paris'
            },
        }
# Loop through the users dictionary
# Python assigns each key to the variable username, and the dictionary associated with each username is assigned to the variable user_info.        
for username, user_info in users.items():  
    print(f"\nUsername: {username}")  # Once inside the main dictionary loop, we print the username

# Start accessing the inner dictionary
# Variable user_info, which contains the dictionary of user information, has three keys: 'first','last', and 'location'.
# use each key to generate a neatly formatted full name and location for each person,
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")



