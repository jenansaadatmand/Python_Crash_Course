# Poll a number of people and ask them what their favourite programming language is
# Dictionary of similar objects
# When you need more than one line in a dictionary
# Press enter after the brace and indent the next line one level

favourite_languages = {
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python',
    }
print(favourite_languages)
print(favourite_languages['phil'])
language = favourite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}.")
print()
# Looping through all key-value pairs using the items() method

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}")
print()

# Looping through all keys using keys() method
for name in favourite_languages.keys():
    print(name.title())
print()

# Alternative way to loop through all keys by default without keys()
for name in favourite_languages:
    print(name.title())
print()


# Looping through a dictionary to access a value that is associated with the current key
# Print a message to friends about the language they choose
friends = ['phil', 'sarah'] # Make a list of friends that we want to print a message to
for name in favourite_languages.keys():  # Inside the loop, we print each person’s name.
    print(f"Hi {name.title()}.")
    if name in friends:  # We check whether the name we’re working with is in the list of friends
        language = favourite_languages[name].title() # Determine the person’s favorite language using the name of the dictionary and the current value of name as the key
        print(f"\t{name.title()}, I see you love {language}!") # Print a special greeting, including a reference to their language of choice.

# Use keys() method to find out if a particular person was polled
if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll!")
print()

# Looping through a dictionary in a particular order using sorted() function
for name in sorted(favourite_languages.keys()):  # To list all keys in the dictionary and sort that list alphabetically before looping through it.
    print(f"{name.title()}, thank you for taking the poll.")
print()

# Looping through All values in a Dictionary using values() method
# Want a list of all languages only
print("The following languages have been mentioned:")
for language in favourite_languages.values():  # for statement here pulls each value from the dictionary and assigns it to the variable language
    print(language.title()) 
print()

# The values() method approach pulls all the values from the dictionary without checking for repeats
# Use a "set", to see the languages chosen without repetition 
# A set is a collection in which each item must be unique
# Wrap set() around a list that contains duplicate items, Python identifies the unique items in the list and builds a set from those items

print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):  # Use set() to pull out the unique languages in favorite_languages.values().
    print(language.title()) # Result in nonrepetitive list of languages
print()

# Building a set directly using braces and separating the elements with commas
languages = {'python', 'ruby', 'python', 'c'}
print(languages)
