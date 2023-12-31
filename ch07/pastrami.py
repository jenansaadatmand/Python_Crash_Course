# No pastrami: using the list sandwich_orders from exercise 7-8
# Make sure the sandwich 'pastrami' appears in th e list at least three times
# Add a code near the beginning of your program to print a message saying the deli has run out of pastrami,
# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches

sandwich_orders = ['pastrami', 'veggie', 'grilled cheese', 'pastrami', 'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []
print("\nDeli has run out of pastrami sanwich.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I am working on your {current_sandwich} sandiwich.")
    finished_sandwiches.append(current_sandwich)
print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich.title()} sandwich.")
print(finished_sandwiches)
