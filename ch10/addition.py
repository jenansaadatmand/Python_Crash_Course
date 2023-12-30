# Addition: one common problem when prompting for numerical input occurs when people provide text instead of numbers
# When you try to convert the input to an int, you'll get a ValueError
# Write a program that prompts for two numbers
# Add them together and print the results
# Catch the ValuError if either input value is not a number, 
# and print a friendly error message
# Test your program by entering two numbers, and then entering some text instead of a number

# solution has a quit option and a while loop to continue entering numbers even if mistake occured
#print("Give me two numbers, and I'll add them.")
#print("Enter 'q' to quit.")
#while True:
#    first_number = input("\nFirsrt number: ")
#    if first_number == 'q':
#        break
#    second_number = input("Second number: ")
#    if second_number == 'q':
#        break
#    try:
#        answer = int(first_number) + int(second_number)
#    except ValueError:
#        print("Sorry you can only enter numbers.")
#    else:
#        print(answer)

# solution 2 there is no quit here but the program ends

try:
    x = input("Give me a number: ")
    x = int(x)
    y = input("Give me another number: ")
    y = int(y)
except ValueError:
    print("Sorry, I really need a number.")
else:
    sum = x + y
    print(f"The sum of (x) and (y) is {sum}.")
