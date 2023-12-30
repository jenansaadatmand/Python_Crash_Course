# Exercise 9-15: Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled.
# Make a list or tuple called my_ticket
# Write a loop that keeps pulling numbers until your ticket wins
# Print a message reporting how many times the loop had to run to give a winning ticket

from random import choice

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = []

print("Let's see what the winnning ticket is...")

# We don't want to repeat winning numbers or letters, so we'll use a 
# While loop.


while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)

    # only add the pulled items to the winning ticket 
    # if it hasn't already been pulled.

    if pulled_item not in winning_ticket:
        print(f"  We pulled a {pulled_item}!")
        winning_ticket.append(pulled_item)

print(f"\nThe final winning ticket is: {winning_ticket}")


my_ticket = () # creating a tuple

while True:
    if pulled_item not in winning_ticket:
        pulled_item = choice(possibilities)
        my_ticket.append(pulled_item)
    
    else:
        winning_ticket = my_ticket
        break 

print()
print("The loop had to run {} times to result in a winning ticket.")
