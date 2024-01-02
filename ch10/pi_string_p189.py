# Large files: One million digits
# If we start with a text file that contains pi to 1,000,000 decimal places instead of 30 
# Program to create a single string containing all these digits
# Use the same program as pi_string.py but pass it a different text file that contains the pi to 1,000,000
# We will just print the first 50 decimal places

filename = 'text_files/pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readline()
pi_string = ''
for line in lines:
    pi_string += line.strip()    
print(f"{pi_string[:52]}...") # Only print the first 50 decimal places, 2 added for leading number 3 and the point .
print("\n")
print(len(pi_string))
