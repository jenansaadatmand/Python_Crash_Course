# Favorite number remembered: combine the two programs from execise 10-11 into one file.
# If the number is already stored, report the favorite number to t he user.
# If not, prompt for the user's favorite number and store in a file
# Run the program twice to see that it works.

# Program using try-except-else block in a function
import json
def favorite_num(): # We are using a function to ask the user for favorite number, store it and retrieve a stored favorite number if one exist and prompt for a new favorite number if one doesn't exist and store it.
    """prompt user for favorite number."""
    filename = 'favorite_num.json'
    try:
        num = input("What is your favorite number? ") 
        with open(filename, 'w') as f:
            number = json.dump(num, f)
        print(f"I'll remember your favorite number.")

    except FileNotFoundError:
        num = input("What is your name? ") 
        with open(filename) as f:
            json.load(f)
    else:
        print(f"I know your favorite number! it's {num}!")

    
favorite_num()




# Program refactoring with three functions:
#import json
#filename = 'favorite_num.json'
#num = input("What is your favourite number? ")

#def num_store():
#    """Stores user's favorite number"""
#    with open(filename, 'w') as f:
#        json.dump(num, f)
#        print("Thanks! I'll remember that.")


#def num_read():
#    """Reads stored favorite number and prints a message"""
#    with open(filename) as f:
#        num = json.load(f)
#    if num:
#        print(f"I know your favorite number! it's {num}")
#    else:
#        num = input("What is your favorite number?")
#        with open(filename,'w') as f:
#            json.dump(num, f)

#num_store()
#num_read()
