# Testing multiple conditions using a series of if statement only to check if all conditions pass not just one condition only as in if-elif-else chain
# A series of if statements is used when more than one condition could be true and you want to act on every condition that is True
# Someone orders two toppings for pizza, must make sure both toppings are included in the pizza

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
