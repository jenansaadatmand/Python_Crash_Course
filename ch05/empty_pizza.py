# Checking that the list is not empty using an if statement
# Empty pizza to let the user provide the information that's stored in a list
# We cannot assume the list has items in it, each time the loop runs
# Useful to check whether a list is empty before running a for loop
# Check whether the requested topping is empty before building the pizza
# If the list is empty, we will prompt the user and make sure he wants a plain pizza
# If the list is not empty we will build the pizza

requested_toppings = []
if requested_toppings: # instead of jumping right into the loop, we do a quick check
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
