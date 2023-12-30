# Example where catching an error can allow a program to continue running
# Using exceptions to prevent crashes
# Useful when programs prompt users for input, handling error when the program responds to invalid input appropriately, it can prompt for more valid input instead of crashing or stop running
# Simple calculator that does only division

print("Give me numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:     
        answer = int(first_number)/ int(second_number)
        print(answer)
    except ZeroDivisionError:
        print("You can't divide by zero!")

 # This program does nothing to handle errors, so asking it to divide by zero causes it to crash
 # Add try-except block to handle the error
    
