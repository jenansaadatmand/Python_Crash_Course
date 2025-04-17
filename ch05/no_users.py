# No users: Add an if test to hello_admin.py to make sure the list of users is not empty
# If the list is empty, print the message We need to find some users!
# Remove all of the usernames from your list, and make sure the correct message is printed

# This code does not work!

usernames = ['john']
for username in usernames:
    if username in usernames:
        print("We have users!")
else:
    print("We need to find some users!")
print()

# Solution 2

usernames = ['john']  # make list empty to execute else statement
if usernames:
    for username in usernames:
        print("We have users!")
else:
    print("We need to find some users!")
print()

# Solution 3

usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username}, would you like to see a status report?")
        else: 
            print(f"Hello {username}, thank you for logging in again!")    
else:
    print("We need to find some users!")


