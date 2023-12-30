# Using int() to Accept Numerical Input
# when using input() function, python interpret everything the user enters as a string
# program asks for user's age
# int() function, treat the input as a numerical value.
age = input("How old are you? ")
age = int(age) # converts input string to a numerical value
print(age) # python returns a string "number", representing the numerical value entered
print(f"You are {age} years old!")
