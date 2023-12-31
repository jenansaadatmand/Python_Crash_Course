# Polling: Use the code in favourite_language.py (page 97)
# Make a list of people who should take the favourite languages poll
# Include some names that are already in the dictionsry 
# And some names that are not
# Loop through the lidt of people who should take the poll
# If they have already taken the poll, print a mesage thanking them for reponding
# If they have not yet taken the poll, print a message inviting them to take the poll

favourite_languages = {
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python',
    }
for name, language in favourite_languages.items():
    print(f"{name.title()} favourite language is {language}.")
print("\n")

coders = ['jen', 'edward', 'tom', 'nowe', 'jim', 'phil'] 
for coder in coders:
    if coder in favourite_languages.keys():
        print(f"Thank you for taking the poll!, {coder.title()}")
    else:
        print(f"{coder.title()} what's your favourite programming language?")
print()
