# Exercise 3-6 More guests: you just found a bigger dinner table, so now
# More space is available. Think of three guests to invite to dinner
# Start with your program from exercise 3-4 or 3-5
# Add a print() call to the end of your program, informing people that you found a bigger table
# Use insert() to add one new guest to the beginning of your list
# Use insert() to add one new guest to the middle of your list
# Use append() to add one new guest to the end of your list
# Print a new set of invitation messages, one for each person in your list

guest_list = ['jimmy','tiffany', 'spoiler']
print(f"Hello {guest_list[0].title()}, you are invited for dinner.")
print(f"Hello {guest_list[1].title()}, you are invited for dinner.")
print(f"Hello {guest_list[2].title()}, you are invited for diner.")
print()
for guest in guest_list: 
    print(f"Hello {guest.title()}, I have found a bigger table.")
print()
guest_list.insert(0, 'nana') # Adding one guest to the beginning of list
print(guest_list)
guest_list.insert(2, 'soso') # Adding one guest in the middle of list
print(guest_list)
guest_list.append('fofo') # Appending one guest to the end of the list
print(guest_list)
print()
# printing new set of invitation messages for each guest 
for guest in guest_list:
    print(f"Hello {guest.title()}, you are invited to diner.")
print()
print(len(guest_list))
