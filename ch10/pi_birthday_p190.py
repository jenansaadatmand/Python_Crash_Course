# Is your birthday contained in pi?
# program to find out if someone's birthday appears anywhere in the first million digits of pi
# first express each birthday as a string of digits and see if that string appears anywhere in pi_string

filename = 'text_files/pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines: 
    pi_string += line.strip()
birthday = input("Enter your birthday, in the form mmddyy: ") # prompt for the user's birthday
if birthday in pi_string: # check if that string is in pi
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

