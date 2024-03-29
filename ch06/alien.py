# Dictionary a collection of key-value pairs
# Game dictionary that stores alien's color and point value
alien_0 = {'color':'green', 'points':5}
print(alien_0)
print(alien_0['color']) # providing the key to access the value associated with it
print(alien_0['points']) # dictionary name[key] to get the associated value
new_points = alien_0['points']    # when one green alien is shot
print(f"You just earned {new_points} points!")  
print("\n")

# Using the x and y coordinates of the alien, place the alien in a particular
# Position on the left edge of the screen, 25 pixels down from the top
# Screen coordinates usually start at the upper-left corner of the screen
# We will place an alien on the left edge by setting the X-coordinate to 0 and 25 pixels from the top
# By setting its Y-coordinate to positive 25
alien_0['x_position'] = 0 # adding new key-value pairs
alien_0['y_position'] = 25
print(alien_0)
