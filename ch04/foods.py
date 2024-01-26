# Copying a list: start with a list and make a completely new list based on the first list
# list[:] to make a slice or copy of the entire list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # making a slice of the entire list to copy the list

print("My favourite foods are:")
print(my_foods)
print("\nMy freind's foods are:")
print(friend_foods)
# To prove we have two seperate lists, we add new food to each list and show that each list keeps track of person's favorite foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("\nMy favorite foods are:")
print(my_foods)
print("\nMy freind's favorite food are:")
print(friend_foods)
