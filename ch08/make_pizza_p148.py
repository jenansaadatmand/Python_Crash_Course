# Mixing positional and arbitrary arguments
# If you want a function to accept several different kinds of arguments, the parameter that accepts the arbitrary arguments must be placed last in the function definition.
# Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter
# If the function needs to take in a size for the pizza, that parameter must  come before the parameter *toppings:
# You'll often see the generic parameter name *args, which collects arbitrary positional arguments like this


#def make_pizza(size, *toppings): # python assigns the first value it recieves to the parameter size, all other values that come after are stored in toppings tupple
#    """Summarize the pizza we are about to make."""
#    print(f"\nMaking a {size}-inch pizza with the following toppings:")
#    for topping in toppings:
#        print(f"- {topping}"")

#make_pizza(16, 'pepperoni') 
#make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') # the function call include an argument for the size first, followed by as many as toppings as needed


# Solution 2 using *args

def make_pizza(size, *args): # * args for arbitrary arguments to be saved in a tupple
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}=inch pizza with the following toppings:")
    for topping in args:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')    
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
