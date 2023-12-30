# Guestbook: write a while loop that prompts users for their name
# When they enter their name, print a greeting to the screen
# and add a line recording their visit in a file called guest_book.txt
# Make sure each entry appears on a new line in the file

filename = 'text_files/guest_book.txt'
print("Please enter 'quit' when you are finished.")

while True:
    name = input("What is your name? ")
    if name == 'quit':
        break
    else:    
        with open(filename, 'a') as file_object:
            file_object.write(f"{name.title()}\n")
        print(f"Hello {name}, you've been added to the guest book.")

