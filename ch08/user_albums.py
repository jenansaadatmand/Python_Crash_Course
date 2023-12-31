# User albums: start with your program from Exercise 8-7.
# Write a while loop that allows users to enter an album's artist and title
# Once you have that information, call make_album() with the user's input and print the dictionary that's created
# Be sure to include a quit value in the while loop

def make_album(artist, title, tracks = '0'):
    """Builds a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


#while True: # This is an infinite loop

#    print("\nEnter 'q' to exit.")
#    artist = input("\nEnter artist's name: ")
#    if artist == 'q':
#        break
#    title = input("Enter album title: ")
#    if title == 'q':
#        break
#    album = make_album(artist, title)
#    print(album)
#print("\nThanks for responding!")

        
# Solution 2:

# Prepare the prompts.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist?"

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':  # Must type quit not q on the prompt to work
        break
    artist = input(artist_prompt)
    if artist == 'quit':
        break
    album = make_album(artist, title)
    print(album)
print("\nThanks for responding!")


# Solution 3

#while True: # this is an infinite loop

#    prompt = "Enter artist name, "
#    prompt += "(Enter 'q' to quit):"
    
#    artist = input(prompt) # concatenate both prompts in one

#    if artist == 'q':
#        break
#    title = input("Enter album title: ")
#    if title == 'q':
#        break
#    album = make_album(artist, title)
#    print(album)
#print("\nThanks for responding!")
        

# Solution 4 

#prompt = "Enter " # assign a prompt as constant

#while True: # this is an infinite loop
#    artist = input(prompt + "artist: ") # add to the constant prompt, the word artist

#    if artist == 'q':
#        break
#    title = input(prompt + "title: ") # # add to the constant prompt, the word title
#    if title == 'q':
#        break
#    album = make_album(artist, title)
#    print(album)
#print("\nThanks for responding!")

# Note because of infinite loop, all above program will continue asking for input over and over, unless you introduce a break at the end or you remove the while loop so it becomes a onetime input only        




