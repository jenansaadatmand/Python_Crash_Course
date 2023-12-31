# Album: write a function called make_album() that builds a dictionary describing a music album
# The function should take in an artist's name and an album title
# And it should return a dictionary containing these two pieces of information


# Use the function to make three dictionaries representing different albums
# Print each return value to show that the dictionaries are storing the album information correctly
# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album
# If calling line includes a value for the number of songs, 
# Add that value to the album's dictionary
# Make at least one new function call that includes the number of songs on an album

#def make_album(artist, title):
#    """Builds a dictionary containing information about an album."""
#    album_dict = {
#        'artist': artist.title(),
#        'title': title.title(),
#        }
#    return album_dict

#album = make_album('metallica', 'ride the lightning')
#print(album)
#album = make_album('beethoven', 'ninth symphony')
#print(album)
#print("\n")
#album = make_album('willie nelson','red-headed stranger')
#print(album)



# using None or 0, as place holder with no specific value, which evaluates as false
# Use None to add optional parameter to make_album that allows to store the number of songs
# program outcome of dictionary with tracks included.

def make_album(artist, title, tracks=0):  # also you can set tracks to none instead of 0
    """Builds a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(), 
        }  # notice if you added tracks here has no attribute title() because it is not a string and it is a number, you can also omit the 'tracks': tracks.title() completely from the dictionary.

    if tracks:
        album_dict['tracks'] = tracks
    return album_dict
#   else:      # another war is to omit line 41 and use the else: statetment
#        return album_dict

album = make_album('samuel','bug', '4')
print(album)

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)
album = make_album('willie nelson', 'red-headed stranger')
print(album)
album = make_album('iron maiden', 'piece of mind', tracks = 8)
print(album)

