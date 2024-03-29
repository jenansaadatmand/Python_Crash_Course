# Slicing a list and working with specific elements
players = ['charles', 'maria', 'michael', 'florence', 'eli']
print(players[0:3]) # Printing a slice of the list containing the first 3 items at index 0,  1, 2 
print()
print(players[0:3:2]) # Including a third argument to skip a value at index 2
print()
# Looping through slices within lists
for player in players[:3]:
    print(player.title()) # Loop through first three players, index 0, 1, 2



print(players[1:4])     # Print the second, third, and fourth items
print(players[:4])      # Omit the first index in a slice python will start at the beginning of the list
print(players[2:])      # If you want a slice to include a second item at the end of a list
print(players[-3:])     # Output the last three elements in the list
print(players[-4:-1:2]) # Third value indicates how many items to skip in a specified range
print(players[:])       # print slice from beginning to end 
