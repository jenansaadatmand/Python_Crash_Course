# Slicing a list and working with specific elements
players = ['charles', 'maria', 'michael', 'florence', 'eli']
print(players[0:3]) # printing a slice of the list containing the thr first 3 items at index 0,  1, 2 
print()
print(players[0:3:2]) # including a third argument to skip a value at index 2
print()
# looping through slices within lists
for player in players[:3]:
    print(player.title()) # loop through first three players, index 0, 1, 2