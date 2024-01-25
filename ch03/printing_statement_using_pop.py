# Using pop() method to print a statement
# Removing the last item in the list and storing it in a variable to be used later

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
last_owned = motorcycles.pop()
print(last_owned)
print(f'The last motorcycle I owned was a {last_owned.title()}.')
print()

# Using pop() to remove an item from any position in a list by including the index of the item you are to be removed in parenthesis

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles.pop(1))
first_owned = motorcycles.pop(0)
print(f'The first motorcycle I owned was a {first_owned.title()}')
print(motorcycles)
