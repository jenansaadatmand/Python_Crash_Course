

# Exercise 3-5: Changing Guest List: you just heard that one of your guests can't make the dinner
# So you need to send out a new set of invitations. you"'ll have to think of someone else to invite
# Start with your program from exercises 3-4.
# Add a print() call at the end of your program stating the name of the guest who can't make it
# Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting
# Print a second set of invitation messages, one for each person who is still on your list

guest_list = ['jimmy', 'tiffany', 'spoiler']
print(guest_list)
print(f"Hello {guest_list[0].title()}, you are invited to dinner.")
print(f"Hello {guest_list[1].title()}, you are invited to dinner.")
print(f"Hello {guest_list[2].title()}, you are invited to dinner.")
print()

print(f"Hello everone, sadly Spoiler cannot make it for dinner.")
# Modify element by replacement at index 
guest_list[2]= 'nana' 

# Delete then append or insert approach
#del guest_list[2] 
#print(guest_list)
#guest_list.append('nana') # appends at end of list
#guest_list.insert(0, 'nana')
print(guest_list)
print()
# Printing a second set of invitations
print(f"Hello {guest_list[0].title()}, you are still invited to dinner.")
print(f"Hello {guest_list[1].title()}, you are still invited to dinner.")
print(f"Hello {guest_list[2].title()}, you are still invited to dinner.")
print()
# Alternative solution: 
for guest in guest_list:
    print(f"Hello {guest}, you are still invited to dinner.")
