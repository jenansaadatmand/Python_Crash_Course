# Exercise 3-10 Every function: Think of things you could store in a list
# For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you'd like
# Write a program that creates a list containing these items and n uses each function 
# In this chapter at least once

languages= ['english', 'french', 'arabic', 'persian', 'german', 'turkish']
print("Here is the original list:")
print(languages)
print()
# use each function introduced in Chapter 3 at least once:
# Accessing elements in a list using their index
print(f"Item at index 5 is: {languages [5].title()}")
print(f"Item at last index: {languages[-1].upper()}")
print(f"Item at index 3: {languages[3].lower()}")
print(f"Item at index -2: {languages[-2].title()}")
print()
# Using individual values from a list using f-string to compose message-building sentences
print("Using f-string to build sentences:")
print(f"My first language was {languages[2].title()}")
print()
# Modifying elements in the list
# Changing the values and replacing elements, the first item at index 0, replacing english with italian
print("Replacing items using index:")
languages[0]= 'italian'
print(languages)
print()
# Adding elements to a list 
# Appending elements to the end of a list
print("Appending item using append():")
languages.append('russian')
print(languages)
print()
# Inserting elements into a list using insert()
print("Inserting item using insert():")
languages.insert(1, 'spanish')
print(languages)
print()
# Removing elements permanently from a list from any position using del statement
print("Deleting item permanently using del statement:")
del languages[1]
print(languages)
print()
# Remove items using pop() method from the end of the list and assigning to a variable to be used somewhere else
print("Removing item temporarily using pop():")
popped_lang = languages.pop()
print("Here is the popped item:")
print(popped_lang.title())
print(languages) 
print("After using a series of pop():")
popped_lang=languages.pop()
print("Here is the popped item:")
print(popped_lang.title())
print(languages)
print()
# Popping items from any position in  alist by index
print("Popping items by position/index:")
popped_lang = languages.pop(3)
print(languages)
print(f"The third language learned is {popped_lang.title()}")
print(f"The last language I learned was {languages[-1].title()}")
print()
# removing item by value using remove()
print("Removing item by value using remove():")
languages.remove('italian')
print(languages)
difficult_lang = 'german'
languages.remove(difficult_lang)
print(f"\n{difficult_lang.title()} is a difficult language to learn")
print(languages)
print()
# organizing a list and sorting it
# sort() a list alphabetically and permanently 
print("Sorting list alphabetically and permenantly:")
languages.sort()
print(languages)
print()
# sort() list permanently in reverse-alphabetical order
print("Sorting list permenantly in reverse alphabetical order:")
languages.sort(reverse=True)
print(languages)
print()
# sorting a list alphabeticaly temporarily using sorted()
print("Sorting list temporarily in alphabetical order using sorted():")
print(sorted(languages))
print(languages) # list original order unchanged
print()
# sorting a list in reverse-alphabetical order temporarily
print("Sorting list temporarily in alphabetical reverse order using sorted():")
print(sorted(languages, reverse=True))
print(languages)
print()

# sorting a list in reverse chronological order using reverse()
print("Sorting list in chronological reverse order using reverse():")
languages.reverse()
print(languages)
# finding the length of the list
print(len(languages))





