# Lottery: make a list or tuple containing a series of 10 numbers and five letters
# Randomly select four numbers or letters from the list and 
# Print a message saying that any ticket matching these four numbers or letters wins a prize


from random import randint, choice

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

x1 = choice(num)
x2 = choice(num)
x3 = choice(num)
x4 = choice(num)

winning_num = f"{x1}, {x2}, {x3}, {x4}"

print(f"Any ticket matching these four numbers or letters wins a prize!: '{winning_num}'")

print()

# Solution 2

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = []

print("Let's see what the winnning ticket is...")

# We don't want to repeat winning numbers or letters, so we'll use a 
# While loop.


while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)

    # Only add the pulled items to the winning ticket 
    # If it hasn't already been pulled.

    if pulled_item not in winning_ticket:
        print(f"  We pulled a {pulled_item}!")
        winning_ticket.append(pulled_item)

print(f"\nThe final winning ticket is: {winning_ticket}")
