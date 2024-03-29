# Syntax to modifying an element in a list is similar to the syntax for accessing an element in a list
# name of list[index of element to change] = new value 
# Modifying elements in a list. Changing the value of the first item in the list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print(motorcycles[0])
motorcycles[0] = 'ducati' # to change item in list: name of list[index]'new value'
print(motorcycles)
motorcycles[2] = 'harly davidson'
print(motorcycles)
print()
# Python provides several ways to add new data to the existing list
# 1. Appending elements to the end of the list using append() method
# 2. Inserting elements into a list using insert() method
# 3. Removing elements from a list according to their position in the list using del statement list name[index]
# 4. Removing the element according to its position using the pop() method from any position in the list. useful when you want to use the value of an item after you remove it from a list 
# 5. Removing element by value by remove() method
# Organizing a list 
# 1. Sorting permanently with the sort() method
# 2. Sorting a list temporarily with the sorted() function
# 3. Printing a list in Reverse order
# 4. Finding the length of a list
motorcycles1 =  ['suzuki', 'yamaha', 'Honda']
print(motorcycles1)
motorcycles1.append('ducati')  # Adding new item to end of list using append() method
print(motorcycles1)
print()

# Building lists (eg after the program is running and the user inputs data): using an empty list, let's start building a list by adding items to it
motorcycles2 = []
motorcycles2.append('honda')
motorcycles2.append('yamaha')
motorcycles2.append('suzuki')
print(motorcycles2)
print()
motorcycles2.insert(0, 'ducati')        # Inserting element using insert()
print(motorcycles2)
del motorcycles2[0]                     # Removing an element from the list according to position using del statement
print(motorcycles2)
print()
del motorcycles2[1]                     # Delete the second item in the list
print(motorcycles2)
print()
# When want to use the value of an item after you removed it from the list, remove an item using the pop() method
# pop() method removes the last item in the list but it lets you work with that item after removing it from the list
motorcycles3 = ['honda', 'suzuki', 'yamaha']
print(motorcycles3)
popped_motorcycles3 = motorcycles3.pop() # removes the last item from the list and stores to a popped_motorcycles3 assigned variable
print(motorcycles3)
print(popped_motorcycles3) # prints the last item that was removed and proves that we have access to it when we need it
print()
motorcycles4 = ['suzuki', 'yamaha', 'honda', 'ducati']      
print(motorcycles4)
motorcycles4.remove('ducati')       # Removing an item by value using remove() method if you don't know its position in the list

print(motorcycles4)
print()

# You can also use remove() method to work with a value that's being removed from the list
moto = ['honda', 'yamaha', 'suzuki', 'ducati']
print(moto)
too_expensive = 'ducati'   # Assign a variable to ducati
moto.remove(too_expensive) # Use variable to tell python which value to remove from the list but still accessible through the variable allowing us to print a statement
print(moto) # Remove 'ducati' and give it a reason for removing it from the list
print(f"\nA {too_expensive.title()} is too expensive for me.") # \n for new line to be printed before the statement
