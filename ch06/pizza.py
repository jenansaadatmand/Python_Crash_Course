# A list in a dictionary
# Describe a pizza that someone is ordering
# Two kinds of information are stored for each pizza: a type of crust and a list of toppings
# List of toppings is a value associated with the key 'toppings'

# Store information about a pizza being ordered.
pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese'],
        }
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza" 
    " with the following toppings:") # breaking a long line and end the line with a quotation mark, indent the next line, add an opening quotation mark and continue the string
# To print the toppings, we use a for loop and access the dictionary using the key toppings
for topping in pizza['toppings']:
    print("\t" + topping)
