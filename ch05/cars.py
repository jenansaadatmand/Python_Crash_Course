# Sorting a list alphabetically and permenantly using sort() method
cars=["bmw", 'audi', 'toyota', 'saburu']
cars.sort()
print(cars)
# sorting the list in reverse-alphabetical order by passing the argument reverse=True in sort() method
# using sort(reverse=True)

cars.sort(reverse=True)
print(cars)
print()

# sorting a list temporarily and without affecting the original order
# use sorted() funtion

cars = ['bmw','audi', 'toyota', 'saburu']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list agian:") # unchanged original order of list
print(cars)

# sorted() function can also accept reverse=True argument
print("\nHere is the sorted list in reverse-order:")
print(sorted(cars, reverse=True))
print(cars) # list original order is unchanged
print()

# Printing a list original order in reverse order using reverse() method 
# permenantly reversing the original chronological order of the list
cars = ['bmw', 'audi', 'toyota', 'saburu']
print("Here is the original list chronological order in reverse:")
cars.reverse()
print(cars)
print()

# to revert back to original list order apply reverse() method a second time
print("reverted list to original order after second reverse():")
cars.reverse()
print(cars)

# finding the length of a list
print(len(cars))
