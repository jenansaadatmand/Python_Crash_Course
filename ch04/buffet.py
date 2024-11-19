# Buffet: a buffet style restaurant offers only five basic foods
# Think of five simple foods, and store them in a tuple
# Use a for loop to print each food the restaurant offers
# Try to modify one of the items, and make sure that Python rejects the change
# The restaurant changes its menu, replacing two of the items with different foods
# Add a line that writes the tuple
# And then use a for loop to print each of the items on the revised menu

menu_items = ("pizza", "curry", "fish", "chicken", "meat")
print("You can choose from the following menu items:")
for item in menu_items:
    print(f"- {item}".title())

# Buffets[0] = "melon" # python does not support reassignment of tuple
print("\n")

# Restaurant changes its menu

menu_items = ("sandwitch", "curry", "fish", "chicken", "cake")
print("\nOur menu has been updated:")
print("You can choose from the following items:")
for item in menu_items:
    print(f"- {item}".title())


