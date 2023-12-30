# Exercise 3-7 shrinking guet list: you just found out that your new dinner table won't arrive in time for diner
# and now you have space for only two guests
# Start with your program from exercise 3-6
# Add a new line that printss a ssage saying that you invite only two people for dinner
# Use pop() remove guests from your list one at a time until only two names remain in your list
# Each time you pop a name from your list, print a message to that person 
# Letting them know you're sorry you can't invite them dinner
# print a message to each of the two people still on your list, letting them know they're still invited
# use del to remove the last two names from your list, so you have an empty list
# print your list to make sure you actually have an empty list at the end of your program 

guest_list = ['jimmy', 'tiffany', 'spoiler']
for guest in guest_list: 
    print(f"Hello {guest.title()}, you are invited for diner") 
print()
guest_list.insert(0, 'nana')
guest_list.insert(2, 'soso')
guest_list.append('fofo')
print(guest_list)
print()
for guest in guest_list: 
    print(f"Hello {guest.title()}, you're invited to diner.")

print()
for guest in guest_list: 
    print(f"Hello {guest.title()}, I am sorry but I can invite only two people for dinner.")
print()
# use pop() to remove guests from list one at a time
print("This is the original guest list:")
print(guest_list) # printing original guest list
print()
popped_guest_1 = guest_list.pop()
print(f"Hello {popped_guest_1.title()}, I am sorry I can't invite you for dinner.")
print()
popped_guest_2 = guest_list.pop()
print(f"Hello {popped_guest_2.title()}, I am sorry I can't invite you for diner.")
print()
popped_guest_3 = guest_list.pop()
print(f"Hello {popped_guest_3.title()}, I am sorry I can't invite you for diner.")
print()
popped_guest_4 = guest_list.pop()
print(f"Hello {popped_guest_4.title()}, I am sorry I can't invite you for diner.")
print()
print("This is the final list of invited guests:")
print(guest_list)
print()
for guest in guest_list: 
    print(f"Hello {guest.title()}, you are still invited for diner.")

# using del statement to remove permenantly the last two names
del guest_list[0]
del guest_list[0]
print("This is the empty list:")
print(guest_list) # confirming that the list is empty 
print()
print(len(guest_list))
