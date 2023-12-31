# Glossar 2: Now that you know how to loop through a dictionary
# Clean up the code from exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary's keys and values
# When you're sure that your loop works, add five more python terms to your glossary
# When you run your program again, these new words and meanings should automatically be included in the output

glossary = {
    'variable': 'store data',
    'list': 'collection of items in particular order',
    'dictionary': 'collection of key-value pair',
    'constant': 'All capital letters variable whose value stays the same throughout the life of the program',
    'conditional test': 'expression within if statement that can be evaluated as True or False',
    }
for word, definition in glossary.items(): 
    print(f"\nWord: {word}")
    print(f"Definition: {definition}")   
print()

# Solution 2
for word, definition in glossary.items():
    print(f"\n{word.title()}; {definition} ")
print()

# Adding 5 new words and meanings

glossary['floating point'] = 'numerical value with a decimal point' 
glossary['key'] = 'The first item in a key-value pair in a dictionary'   
glossary['string'] = ' a series of characters'
glossary['loop'] = 'work through a collection of items, one at a time'
glossary['boolean expression'] = 'An expression that evaluates to True or False'
for word, definition in glossary.items():
    print(f"\nWord: {word}")
    print(f"Definition: {definition}")
print()
print()
for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")
