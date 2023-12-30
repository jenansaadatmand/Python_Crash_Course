# Exercise 3-4: Guest list: If you could invite anyone, living or deceased, to dinner,
# Who would you invite ? Make a list that includes at least three people
# You'd like to vite to dinner.   
# Then use your list to print a message to each person, inviting them to dinner

guest_list = ['jimmy', 'tiffany', 'spoiler']
print(f"Hello {guest_list[0].title()}, you are invited to dinner.")
print(f"Hello {guest_list[1].title()}, you are invited to dinner.")
print(f"Hello {guest_list[2].title()}, you are invited to dinner.")
print()

# solution # 2
# using a for loop
for guest in guest_list:
    print(f"Hello {guest.title()}, you are invited to dinner.")

# Solution 3: 

guests = ['jimmy', 'tiffany', 'spoiler']
msg = ", you are invited to dinner!"
print(f'{guests[0].title()}{msg}')
print(f'{guests[1].title()}{msg}')
print(f'{guests[2].title()}{msg}')
print()
