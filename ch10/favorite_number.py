# Favourite number: write a program that prompts for the user's favourite number
# Use json.dump() to store this number in a file
# Write a separate program that reads in this value and prints the message, "I know your favourite number! it's -----"

# Program that prompts for user favorite number
#import json

#filename = 'favorite_num.json'
#num = input("What is your favourite number? ")

#with open(filename, 'w') as f:
#    json.dump(num, f)
#    print("Thanks! I'll rememmber that.")


# Program that Reads user's favourite number
import json
filename = 'favorite_num.json'
with open(filename) as f:     
   num = json.load(f)
print(f"I know your favorite number! it's {num}.")

# i forgot the f before " and it did not replace the number in line 21 when printed
