# Pizzeria displays a message whenever a topping is added to your pizza as it's being made
# Making a list of toppings the customer has requested
# and using a loop to announce each topping as it's being addd to the pizza
# Checking for special items using if statement 

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

# What if the pizzeria runs out of green peppers? an if statement inside the loop can handle this situation

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
else: 
    print("\nFinished making your pizza!") # ensures all other toppings will be added to the pizza
    