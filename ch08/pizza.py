# Passing an Arbitrary Number of Arguments:
# In situations where you don't know in advance how many arguments a function needs to accept
# Python allows a function to collect an arbitrary number of arguments from calling statement
# A function that builds pizza. it needs to accept a number of toppings, but you can't know ahead of time how many topping a person will want
# The function has one parameter *toppings, but this parameter collects as many arguments as the calling line provides.
# The asterisk * in the parameter tells python to create an empty tupple called toppings and pack whatever values it recieves into this tupple
# The printed output is a tupple even if the function recieves one argument only eg:('pepperoni',)

#def make_pizza(*toppings):  # The * asterick allows the function to accept arbitrary number of parameters that allow passing an arbitrary number of arguments 
#    """Print the list of toppings that have been requested."""
#    print(toppings)
#make_pizza('pepperoni') # Only one value in the argument
#make_pizza('mushrooms', 'green peppers', 'extra cheese') # Passing arbitrary number of arguments or values in the calling of the function

# Now we can replace the print() call with a loop that runs through the list of toppings and describes the pizza being ordered

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
