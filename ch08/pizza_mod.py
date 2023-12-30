# Module contains only the function make_pizza
# The module name will be pizza_mod

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
