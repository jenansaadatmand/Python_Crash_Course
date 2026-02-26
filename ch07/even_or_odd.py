# Modulo Operator %, divided one number by another and returns the remainder
# When one number is divisible by another number, the remainder is 0
# so the modulo operator always returns 0. 
# You can use this fact to determine if a number is even or odd:
# Even numbers are always divisible by two, so if the modulo of a number and two is zero (here, if number % 2 == 0) the number is even. Otherwise, it’s odd.
# programs guess the number is even or odd based on % and 0 remainder


number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
