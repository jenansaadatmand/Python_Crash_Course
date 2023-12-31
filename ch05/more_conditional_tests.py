# More conditional tests:
# You don't have to limit the number of tests you create to ten
# If you want to try more comparisons,
# write more tests and add them to conditional_tests.py
# Have at least one True and one False result for each of the following:
# Tests for equality and inequality with strings
# Tests using the lower() method


# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
# Tests using the and keyword and the or keyword
# Test whether an item is in a list
# Test whether an item is not in a list

motorcycle = 'suzuki'

# Test for equality and inequality with strings

print("Is motorcycle == 'suzuki'? I predict True.")
print(motorcycle == 'suzuki')
print("Is motorcycle != 'suzuki' ? I predict False.")
print(motorcycle != 'suzuki')
print()

# test for inequality
if motorcycle != 'harely':
    print("Test is False!")
print()


# Tests for equality and ignoring case using the lower() method

print("Is motorcycle.lower() == 'suzuki' ? I predict True.")
print(motorcycle.lower() == 'suzuki')
print("Is motorcycle.lower() == 'SUZUKI' ? I predict False.")
print(motorcycle.lower() == 'SUZUKI')
print()

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to

print("Does motorcycle contain 1 bike ? I predict 6")
if len('suzuki') == 6:
    print(len('suzuki'))
print()

month_days = 30 
print(month_days == 30)
print(month_days == 40)
print(month_days != 30)
print(month_days > 30)
print(month_days < 30)
print(month_days <= 30)
print(month_days >= 30 or month_days <= 30)
print(month_days >= 30 and month_days <= 30)


print()

# Tests using the and keyword and the or keyword

print(motorcycle == 'suzuki' and motorcycle == 'harely')
print(motorcycle == 'suzuki' or motorcycle == 'harely')
print(motorcycle == 'suzuki' and motorcycle != 'harely')
print(motorcycle != 'suzuki' or motorcycle != 'harely')
print()

# Test whether an item is in a list using in

print("Is suzuki in mototrcycle? I predict True.")
print('suzuki' in motorcycle)
print()

# Test whether an item is not in a list using not in

banned_motorcycle = 'harely'
print(f"Is suzuki in banned_motorcycle ? I predict True.")
print('suzuki' not in banned_motorcycle)
