# Guest: write a program that prompts the user for their name
# When they respond, write their name to a file called guest.txt

#prompt = 'What is your name? '
#message = input(prompt)
#filename = 'text_files/guest.txt'
#with open(filename, 'a') as file_object:
#    file_object.write(f"\n{message.title()}")


# solution # 2, this program writes the name of the guest and overwrites the previous file
name = input("What is your name? ")
filename = 'text_files/guest.txt'
with open(filename, 'w') as f:
    f.write(name)    
