# Multiples of ten:
# Ask the user for a number, and then report wether the number is a multiple of 10 or not

number = input("Please provide a number?")
number = int(number)
if number % 10 == 0:
    print(f"The number provided {number} is a multiple of ten")
else:
    print(f"You're number provided {number} is not a multiple of ten")

# Solution 2 
number = input("Give me a number, please: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
