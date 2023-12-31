# Glossary: A Python dictionary can be used to model an actual dictionary
# However, to avoid confusion, let's call it a glossary
# Think of five programming words you've learned about the previous chapters
# Use these words as the keys in your glossary
# and store their meanings as values
# Print each word and its meaning as neatly formatted output
# You might print the word followed by a colon and then its meaning
# or print the word on one line and then print its meaning indented on a second line
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output

glossary = {
    'variable': 'store data',
    'list': 'collection of items in particular order',
    'dictionary': 'collection of key-value pair',
    'constant': 'All capital letters variable whose value stays the same throughout the life of the program',
    'conditional test': 'expression within if statement that can be evaluated as True or False',
    }
print(f"Variable; {glossary['variable']}")
print(f"List; {glossary['list']}")
print(f"Dictionary; {glossary['dictionary']}")
print(f"Constant; {glossary['constant']}")
print(f"Conditional test; {glossary['conditional test']}")
print()
# Alternative solution 2
value = glossary['variable']
print(f"Variable; {value}")
value = glossary['list']
print(f"List; {value}")
value = glossary['dictionary']
print(f"Dictionary; {value}")
value = glossary['constant']
print(f"Constant; {value}") 
value = glossary['conditional test']
print(f"Conditional test; {value}")
print()
# alternative solution 3
print("Variable") 
print(f"\t{glossary['variable']}\n")
print("List")
print(f"\t {glossary['list']}\n")
print("Dictionary")
print(f"\t {glossary['dictionary']}\n")
print("Constant")
print(f"\t {glossary['constant']}\n")
print("Conditional test")
print(f"\t {glossary['conditional test']}\n")

# Solution 4
word = 'variable'
print(f"\n{word.title()}: {glossary[word]}")
word = 'list'
print(f"\n{word.title()}: {glossary[word]} ")
word = 'dictionary'
print(f"\n{word.title()}: {glossary[word]}")
word = 'constant'
print(f"\n{word.title()}: {glossary[word]}")
word = 'conditional test'
print(f"\n{word.title()}: {glossary[word]}")
