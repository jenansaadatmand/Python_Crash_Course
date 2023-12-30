# Each person has more than one favourite language using a list nested in a dictionary 

favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
# When we loop through the dictionary, we use the variable name languages to hold each value from the dictionary, because we know that each value will be a list.

for name, languages in favourite_languages.items():
    print(f"\n{name.title()}'s favourite languages:")
    if languages:
        print(len(languages))
    for language in languages:  # Inside the main dictionary loop, we use another for loop w to run through each person’s list of favorite languages.
        print(f"\t{language.title()}")

# To refine this program further by including an if statement at the beginning of the dictionary's for loop
# for loop to see whether each person has more than one favorite language by examining the value of len(languages).
