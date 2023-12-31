# Slicing a list and working with specific elements
players = ['charles', 'maria', 'michael', 'florence', 'eli']
print(players[0:3]) # Printing a slice of the list containing the first 3 items at index 0,  1, 2 
print()
print(players[0:3:2]) # Including a third argument to skip a value at index 2
print()
# looping through slices within lists
for player in players[:3]:
    print(player.title()) # Loop through first three players, index 0, 1, 2



print(players[1:4])  # print the second, third and fourth items
print(players[:4])   # omit first index in a slice python will start at beginning of the list
print(players[2:])  # if you want a slice to include second item to the end of a list
print(players[-3:])   # output the last three elements in the list
print(players[-4:-1:2]) # third value indicates how many items to skip in a specified range
print(players[:])  # print slice from beginning to end 

