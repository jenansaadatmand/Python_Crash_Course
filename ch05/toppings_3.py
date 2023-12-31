# Using multiple lists and if statements 
# Watch for unusual toppings requests before building your pizza
# We make two lists: available topppings and user requested toppings 
# Available list can be a tupple as well, stable and immutable

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:  # Loop through the list
    if requested_topping in available_toppings:  # Inside the loop, check to see if each requested topping is in the available list
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")    

