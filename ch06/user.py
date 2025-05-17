# Looping through a dictionary designed to store user information on a website

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
     }
print(user_0)
print()

# for loop to print all values to keys

for key in user_0:
    print(user_0[key])
print()    

# for loop to peint all keys only

for i in user_0:
    print(i)
    
# Looping and returning all key-value pairs using items() method to iterate over a dictionary

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
print()

# Alternative looping using item() method and two other variables

for k, v in user_0.items():
    print(f"\nKey: {k}")
    print(f"Value: {v}")

