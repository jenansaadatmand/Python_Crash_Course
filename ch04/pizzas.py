# Exercise 4-1 Pizzas: Think of at least three kinds of your favorite pizza. 
# Store these pizza names in a list, and 
# Then use a for loop to print the name of each pizza
# Modify your for loop to print a sentence using the name of the pizza,
# Instead of printing just the name of the pizza.
# For each pizza, you should have one line of output 
# containing a simple statement like I like pepperoni pizza
# Add a line at the end of your program, outside the for loop, 
# that states how much you like pizza.
# The output should consist of three or more lines about the kinds 
# of pizza you like and then an additional sentence, such as I really love pizza!


pizzas = ["pepperoni", "vegi", "mexicain"]
for pizza in pizzas: # a for loop
    print(pizza.title())
    print(f"I like {pizza.title()} pizza")
print(f"I like {pizzas[0]} pizza, \nI like {pizzas[1]} pizza, \nI like {pizzas[2]} pizza, \nI really love pizza!")
