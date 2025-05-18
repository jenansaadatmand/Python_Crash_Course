# Checking usernames: Do the following to create a program that simulates 
# How websites ensure that everyone has a unique username
# Make a list of five or more usernames called current_users
# Make another list of five usernames called new_users
# Makes sure one or two of the new usernames are also in the current_users list
# Loop through the new_users list to see if each new username has already been used
# If it has, print a message that the person will need to enter a new username
# If a username has not been used, print a message saying that the username is available
# Make sure your comparison is case-sensitive
# If 'John' has been used, 'JOHN' should not be accepted
# ( To do this, you'll need to make a copy of current_users containing the lowercase versions of all existing users.)

current_users = ['john', 'tim', 'roro', 'soso', 'fam']
new_users = ['john', 'tim', 'ham', 'kam', 'yam']
for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user} is unavailable, please enter a new username:")
    else:
        print(f"{new_user} username is available")

