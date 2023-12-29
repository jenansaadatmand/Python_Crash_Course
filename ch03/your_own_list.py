# Exercise 3-3: Your Own List: Think of your favorite mode of transportation
# such as a motorcycle or a car, and make a list that stores several examples
# Use your list to print a series of statements about these items,
# such as " I would like to own a Honda motorcycle."

transport= ['motorcycle', 'car', 'bus', 'metro', 'train']
print(f"I would like to own a Honda {transport[0].title()}.")
print(f"I prefer to go to work using my {transport[1].title()} rather than my {transport[0]}.")
print(f"Taking the {transport[2].title()} is an environmentally friendly option.")
print(f"The {transport[3].title()} is close to my house.")
print(f"Finally, there is always the {transport[-1].title()} as an option.")