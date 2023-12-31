# 6-2 page 99 Favourite numbers: use a dictionary to store people's favourite numbers
# Think of five names, and use them as keys in your dictionary
# Think of a favourite number for each person
# and store each as a value in your dictionary
# Print each person's name and their favourite number
# For even more fun, poll a few friends and get some actual data for your program

favourite_numbers = {
    'jimmy': 3, 
    'jim': 100_000,
    'tim': 16,
    'roro': 23,
    'soso': 100,
      }  
print(f"Jimmy's favourite number is: {favourite_numbers['jimmy']}")
print(f"Jim's favourite number is: {favourite_numbers['jim']}")
print(f"Tim's favourite number is: {favourite_numbers['tim']}")
print(f"Roro's favourite number is: {favourite_numbers['roro']}")
print(f"Soso's favourite number is: {favourite_numbers['soso']}")
print()

# Alternative solution

num = favourite_numbers['jimmy']
print(f"Jimmy's favourite number is {num}.")
num = favourite_numbers['jim']
print(f"Jim's favourite number is {num}.")
num = favourite_numbers['tim']
print(f"Tim's favourite number is {num}.")
num = favourite_numbers['roro']
print(f"Roro's favourite number is {num}.")
num = favourite_numbers['soso']
print(f"Soso's favourite number is {num}.")
