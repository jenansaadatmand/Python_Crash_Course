cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()   # Sort them alphabetically, sort method changes the order permanently and we can never revert back to original order
print("\nHere is the list sorted alphabetically:")
print(cars)  
# Sort list in reverse alphabetical order permanently by passing the argument reverse=True to the sort() method
print("\nHere is the list in reverse order:")
cars.sort(reverse=True)
print(cars)
print()
# Soting list temporarily with sorted() function on lower case values in lists only, to maintain the original order of the list but presented in a sorted order
# Sorted function lets you display your list in a particular order but does not affect the actual order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)                 # Original order of list
print("\nHere is the sorted list:")
print(sorted(cars))         # Ordered list alphabetically and changed temporarily
print("\nHere is the original list again:")
print(cars)                 # Order of list still unchanged
print("\n Here is the sorted list in reverse order:")
print(sorted(cars, reverse=True))  # Sorted list alphabetically and in reverse order temporarily
print()

# Printing a list in reverse order with reverse() method permanently but not alphabetically, reverse order of the original list
# But you can reverse back the order to original order by applying reverse() a second time
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
# Applying reverse() a second time to revert back to the original list
cars.reverse()
print(cars)
# Find out the length of a list with len()
print(len(cars))



