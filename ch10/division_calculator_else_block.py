# try-except-else block: python attempts to run the code in the try block, the only code that should go in the try block is code that might cause an exception to be raised.
# Sometimes you will have additional code that should run only if the try block was successful, this code goes in the else block.
# The except block tells Python what to do in case a certain exception arises when it tries to run the code in the try block
# The program continues to run and becomes resistant to innocent user input mistakes and malicious attacks
# making the division_calculator_p195.py program more error-resistant by wrapping the line that might produce errors in a try-except block.  The error on the line that performs the division, so that's where we will put the try-except block.
# This example also  includes an else block. Any code that depends on the try block executing successfully goes into the else block

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.") 

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError: # tells Python how to respond when an error arises
        print("You cannot divide by 0!") # If the try block doesn’t succeed because of a division by zero error, we print a friendly message telling the user how to avoid this kind of error and the program continues to run
    else: # any code that depends on the try block executing successfully goes in the else block
        print(answer)  # If the division operation is successful, we use the else block to print the results
