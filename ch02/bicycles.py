# list is a collection of items in a particular order. items place in square brackets []
# A list that contains a few kinds of bicycles
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)     # this is isn't the output you want your user to see, proceed to access individual items in a list

# Accessing elements in a list or ordered collections by instructing python the position, or index, of the desired item
# Index positions start at 0, Not 1
# To access an element in a list, write the name of the list followed by the index of the item enclosed in aquare brackets

# Example: pull out the first bicycle in the list bicycles, resulting in list item without bracket when the user sees it printed on screen
print(bicycles[0]) # asks for item at index 0, first on the list, 1-1 = 0
print(bicycles[1]) # asks for item at index 1, second on list , 2-1 = 1 substract item location in list by 1
print(bicycles[2]) # asks for item at index 2, third item on list, 3-1 = 2 
print(bicycles[3]) # asks for the item at index 3, fourth item on list, 4-1 = 3
print(bicycles[0].title()) # string neatly formatted using method .title()
print(bicycles[3].upper())
print()
print(bicycles[-1]) # asks for the last item on the list, special syntax to retrieve the last item on a list
print()
# Conventions extend to recalling the -2 second last in the list, -3 third to last in list, etc
print(bicycles[-2])
print(bicycles[-3])
print()

# Using individual values from a list, f-strings format method
# Pulling the first bicycle from the list and composing a message using that value
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
