# Avoiding infinite loops, the program keeps running forever
# CTRL + C to stop an infinite loop
# Program counting loop from 1 to 5 

x = 1
while x <= 5:
    print(x)
# This loop runs forever!
# Value of x will start at 1 but never change. As a result, the conditional test x <= 5 will always evaluate to True and the while loop will run forever, printing a series of 1s
    x += 1   # increment by 1 to get out of the infinite loop, But if you accidentally omit the line x += 1 (as shown next), the loop will run forever:
