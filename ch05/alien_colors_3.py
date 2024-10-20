# Alien colors # 3: 
# Turn your if-else chain from exercise 5-4 into an if-elif-else chain
# If the alien is green, print a message that the player earned 5 points
# If the alien is yellow, print a message that the player earned 10 points
# If the alien is red, print a message that the player earned 15 points
# Write three versions of this program
# Making sure each message is printed for the appropriate color alien


# Version if runs  

alien_colors = 'green'
if alien_colors == 'green':
    print("You just earned 5 points!")
elif alien_colors == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")
print()

# Version elif runs

alien_colors = 'yellow'
if alien_colors == 'green':
    print("You just earned 5 points!")
elif alien_colors == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")
print()

# Version else runs

alien_colors = 'red'
if alien_colors == 'green':
    print("You just earned 5 points!")
elif alien_colors == 'yellow':
    print("You just earned 10 points!")
else: 
    print("You just earned 15 points!")

