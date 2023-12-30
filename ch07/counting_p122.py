# using continue in a loop
# use continue statement to return to the beginning of the loop based on the result of a conditional test.
# program with a loop that counts from 1 to 10 but prints only the odd numbers in that range

current_number = 0  # set curreny number to 0
while current_number < 10: # python enters the loop
    current_number += 1  # increment the count by 1, so current number is 1
    if current_number % 2 == 0: # if statement checks the modulo of current_number and 2, if modulo is 0 (current_number is divisible by 2)
        continue   # continue statement to ignore the rest of the loop and return to the beginning
    print(current_number)  # if current_number is not divisible by 2, the rest of loop is excuteed and prints the current_number
