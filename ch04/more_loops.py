# More loops: All versions of food.py page 63 
# In this section have avoided using for loops when printing to save space
# Choose a version of foods.py
# And write two for loops to print each list of foods


my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favourite foods are:")
for item in my_foods:
    print(f"- {item}".title())
print("\nMy friend's favourite foods are:")
for item in friend_foods:
    print(f"- {item}".title())

