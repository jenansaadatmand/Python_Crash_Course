# Guest: write a program that prompts the user for their name
# When they respond, write their name to a file called guest.txt

#Prompt = 'What is your name? '
Mmessage = input(prompt)
#filename = 'text_files/guest.txt'
#with open(filename, 'a') as file_object:
#    file_object.write(f"\n{message.title()}")


# Solution 2: This program writes the name of the guest and overwrites the previous file
name = input("What is your name? ")
filename = 'text_files/guest.txt'
with open(filename, 'w') as f:
    f.write(name)    
