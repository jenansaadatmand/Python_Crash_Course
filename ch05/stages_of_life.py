# Stages of life: write an if-elif-else chain that determines a person's stage of life
# Set a value for the variable age, and then: 
# If the person is less than 2 years old, print a message that the person is a baby
# If the person is at least 2 years old but less than 4, print a message that the person is a toddler
# If the person is at least 4 years old but less than 13, print a message that the person is a kid
# If the person is at leasdt 13 years old but less than 20, print a message that the person is a teenager
# If the person is at least 20 years old but less than 65, print a message that the peron is an adult
# IF the person is age 65 or older, print a message that the person is an elder

age = 17
if age < 2:
    print("You're a baby!")
elif age == 2 or age < 4:
    print("You're a toddler!")  
elif age == 4 or age < 13:
    print("You're a kid!")
elif age == 13 or age < 20:
    print("You're a teenager!")
elif age == 20 or age < 65:
    print("You're an adult!")
else:
    print("You're an elder")
print()

# Solution # 2:
age = 17
if age < 2:
    print("You're a baby")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager")
elif age < 65:
    print("You're an adult!")
else:
    print("You're an elder!") 




