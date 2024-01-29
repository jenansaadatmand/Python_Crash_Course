# Using a while loop with lists and dictionaries
# To keep track of many users and inputs
# A for loop is useful for looping through a list, but not for modifying a list inside a for loop because Python has trouble keeping track of items inside a for loop
# Use a while loop, to modify a list or dictionary as you work with it, this allows you to collect, store, and organize inputs later
# Moving items from one list to another
# List of newly registered but unverified users of a website
# After we verify the users, we move them to a separate list of confirmed users by using a while loop to pull users from the list of unconfirmed users as we verify them and then add them to a separate list of confirmed users


# Start with users that need to be verified,
# And an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']  # begin with a list of unconfirmed users
confirmed_users = []  # an empty list to hold confirmed users

# Verify each user until there are no more unconfirmed users
# Move each verified user into the list of confirmed users

while unconfirmed_users:  # While loop runs as long as the list unconfirmed_users is not empty.
    current_users = unconfirmed_users.pop()  # Within this loop, the pop() function removes unverified users one at a time from the end of unconfirmed_users. because Candace is last in the unconfirmed_users list, her name will be the first to be removed, assigned to current_user, and added to the confirmed_users list. Next is Brian, then Alice.
    print(f"Verifying user: {current_users.title()}") # We simulate confirming each user by printing a verification message 
    confirmed_users.append(current_users)  # Then adding them to the list of confirmed users.
# As the list of unconfirmed users shrinks, the list of confirmed users grows. When the list of unconfirmed users is empty, the loop stops, and the list of confirmed users is printed:
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users: # a for loop to loop through the list
    print(confirmed_user.title())

