# program determines whether people are tall enough to ride a roller coaster
# When you use numerical input to do calculations and comparisons,be sure to convert the input value to a numerical representation first.
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when You're a little older.")
