# 6-10 Favourite numbers: 
# Modify your program from exercise 6-2(page99)
# So each person can have more than one favourite number
# Then print each person's name along with their favourite numbers

# 6-2 page 99 Favourite numbers: use a dictionary to store people's favourite numbers
# Think of five names, and use them as keys in your dictionary
# Think of a favourite number for each person
# And store each as a value in your dictionary
# Print each person's name and their favourite number
# For even more fun, poll a few friends and get some actual data for your program


# Nesting using a list as value to a key in a dictionary

favourite_numbers = {
    'jimmy': [3, 33, 303], 
    'jim': [100_000, 10_000, 1],
    'tim': [16, 44, 5],
    'roro': [23, 55, 100],
    'soso': [100, 6, 10],
      }  
print(f"Jimmy's favourite number are: {favourite_numbers['jimmy']}")
print(f"Jim's favourite number are: {favourite_numbers['jim']}")
print(f"Tim's favourite number are: {favourite_numbers['tim']}")
print(f"Roro's favourite number are: {favourite_numbers['roro']}")
print(f"Soso's favourite number are: {favourite_numbers['soso']}")
print()

# Alternative solution

num = favourite_numbers['jimmy']
print(f"Jimmy's favourite number are {num}.")
num = favourite_numbers['jim']
print(f"Jim's favourite number are {num}.")
num = favourite_numbers['tim']
print(f"Tim's favourite number are {num}.")
num = favourite_numbers['roro']
print(f"Roro's favourite number are {num}.")
num = favourite_numbers['soso']
print(f"Soso's favourite number are {num}.")
print()

# Solution 3: 

for name, numbers in favourite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"{number}")
