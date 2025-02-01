# Exercise 3-9 dinner guests: working with one of the programs from exercises 3-4 through 3-7 (pages 41-42)
# Use len() to print a message indicating the number of people you're inviting to dinner.
# I choose exercises 3-4 

# Exercise 3-4 guest_list.py
guests = ['jenan saad', 'lili sad', 'toto saa']
print(f'{guests[0].title()}, you are invited to dinner!')
print(f'{guests[1].title()}, you are invited to dinner!')
print(f'{guests[2].title()}, you are invited to dinner!')
print() 

# Solution 1:
num_guests = len(guests)
print(f'\nThe number of guests invited to dinner: {num_guests}')

# Solution 2:
print(f'\nThe number of guests invited to dinner: {len(guests)}')


