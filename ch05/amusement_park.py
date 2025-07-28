# Amusement park admissions
# Admission for anyone under 4 is free
# Admission for anyone between the ages of 4 and 18 is $25
# Admission for anyone age 18 or older is $40
# Admission for seniors with discount > 65 is $20 

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
elif age < 65:
    print("Your admission cost is $40.")
else: 
    print("Your admission cost is $20.")
print()    

# Alternative cleaner more efficient revised code which is easier to modify

age = 70
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else: 
    price = 20
print(f"Your admission cost is ${price}.")
print()

# Omitting the else block for a clearer conditional test
age = 65 
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")
