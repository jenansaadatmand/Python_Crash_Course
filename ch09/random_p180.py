# Random module contains the randint() 
#ranint() takes two integer arguments and returns a randomly selected integer between (and including) those numbers.

# How to generate a random number between 1 and 6:

from random import randint  # ranint() function takes in a two integer numbers and returns a number in betwen (and including) the those numbers
print(randint(1,6))

print()

from random import choice  # choice() function takes in a list [] or tuple () and returns a randomly chosen element

players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)  # choice() take in list players
print(first_up)


# You can alternatively import both functions from the module using this syntax
# from random import randit, choice
