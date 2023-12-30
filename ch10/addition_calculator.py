# Addition calculator: wrap your code from Excersize 10-6 in a while loop so the user can continue entering numbers even if they make a mistake and enter text instead.

print("Enter 'q' to quit.\n")

while True:
    try:
      x = input("\nGive me a number: ")
      if x == 'q':
        break
      x = int(x)

      y = input("Give me another number: ")
      if y == 'q':
        break

      y = int(y)
    
    except ValueError:
        print("I really need a number.")
    else:
        sum = x + y
        print(f"The sum of (x) and (y) is {sum}.")
