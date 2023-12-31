# Modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# Modify element at index 0 to dukati
motorcycles[0]='ducati'
print(motorcycles)

# Adding elements to the end of a list  using .append() method
motorcycles.append('ninja')
print(motorcycles)
print()

# Appending elements to the end of a list
# Start with an empty list and then use append() method to add items
motor = []
motor.append('honda')
motor.append('yamaha')
motor.append('suzuki')
print(motor)
print()


# Inserting elements into a list using insert(index of new element, new value) method
# This operation shifts every value one position to the right
motorcycles.insert(0, 'ducati2')
print(motorcycles)
print()

# Removing elements from a list using various methods
# Remove item according to its position or value
# Removing item using del statement, if you know the position/index of the item 

del motorcycles[0]
print(motorcycles)

print()
del motorcycles[1]
print(motorcycles)
print()

# Removing item from end of list using pop() method
# pop() removes last item from the list and keeps it in memory to be used in other places

popped_motorcycle = motorcycles.pop() # pop() the last item and assign to variable
print(motorcycles) # removed last item from list
print(popped_motorcycle) # to prove that we still have access to the removed value 
print()

# Imagine the motorcycles are arranged in a chronological order
# Print a statement about the last motorcycle owned

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
print()
# Poping items from any position in a list by including the index/position in the parenthesis

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was {first_owned.title()}.")
print()

# Removing item by value using remove() method, when index is not known
print(motorcycles) # to show list is empty
if 'ducati' in motorcycles: # to check if item exists in the list
    motorcycles.remove('ducati')
    print(motorcycles)
else:   
    print("Item doesn't exist on the list")
print()

# Making a new list: 
motorcycles = ["honda", "suzuki", "ducati"]
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# Also you can use remove() method to work with a value being removed and 
# print a statement about it (why it was removed)

too_expensive = 'honda' # assign a variable for item to be removed
motorcycles.remove(too_expensive) # remove the variable
print(motorcycles)
print(f"\nA {too_expensive} is too expensive for me.")

# organizing a list: presenting information in a particular order, preserve or change original order of list 

