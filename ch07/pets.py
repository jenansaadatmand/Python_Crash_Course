# removing all instances of specific values from a list
# remove() is used to remove a specific value from a list, used when the value to be removed appeared only once in the list
# to remove all instances of a value from a list? use a while loop
# list of pets with a value 'cat' repeated several times
# to remove all instances of 'cat' repeated, you run a while loop until 'cat' is no longer in the list

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets: # Python enters the while loop because it finds the value 'cat' in the list at least once
    pets.remove('cat')
print(pets)