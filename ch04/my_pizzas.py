# My Pizzas, your pizzas: start with your program from Exercise 4-1 page 56
# Make a copy of the list of pizzas, and call it friend_pizzas
# Then do the following:
# Add a new pizza to the original list
# Add a different pizza to the list friend_pizzas
# Prove that you have two separate lists
# Print the message My favourite pizzas are:
# And then use a for loop to print the second list
# Make sure each new pizza is stored in the appropriate list


favourite_pizzas = ["pepparoni", "veggie", "mexican" ]
friend_pizzas = favourite_pizzas[:] # Copying a list by slice starts at first item and ends at last item
# Add one pizza added to original list:")
favourite_pizzas.append("hawaian") 
# Add one pizza added to second list:")
friend_pizzas.append("cheese")
# Proof of one pizza added to original list:")
print("\nMy favourite pizzas are:")
for pizza in favourite_pizzas:
    print(f"- {pizza}".title())
print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}".title())



