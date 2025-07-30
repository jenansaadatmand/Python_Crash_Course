# Exercise 3-8: Seeing the world: Think of at least five places in the world you'd like to visit
# Store the locations in a list. Make sure the list is not in alphabetical order
# Print your list in its original order. Don't worry about printing the list neatly; just print it as a raw Python list
# Use sorted() to print your list in alphabetical order without modifying the actual list
 

places = ['turkey', 'bahamas', 'italy', 'norway']
print("\nHere is the original list:")
print(places)
print("\nHere is the sorted list:")
print(sorted(places))
print("Here is the original list again:")
print(places)
print("\nHere is the sorted list in reverse-order:")
print(sorted(places, reverse=True))
print("\nHere is the original list again:")
print(places)
print("\nHere is the original list in reverse order:")
places.reverse()
print(places)
print("\nHere is the list after reverting to original order:")
places.reverse()
print(places)
print("\nHere is the list sorted alphabetically:")
places.sort()
print(places)
print("\nHere is the list sorted in reverse-alphabetical order:")
places.sort(reverse=True)
print(places)



# Notes:

# Use sort() to print your list in alphabetical order without modifying the actual list.
# Show that your list is still in its original order by printing it.
# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list
# Show that your list is still in its original order by printing it again
# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list
# Show that your list is still in its original order by printing it again
# Use reverse() to change the order of your list. print the list to show that its order has changed
# Use reverse() to change the order of your list again. Print the list to show it back to its original order
# Use sort() to change your list so it's stored in alphabetical order.
# Print the list to show that its order has changed
# Use sort() to change your list so it's stored in reverse-alphabetical order.
# Print the list to show that its order has changed
