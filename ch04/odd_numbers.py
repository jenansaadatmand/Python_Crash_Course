# Exercise 4-6 Odd numbers: use the third argument of the range() function to 
# make a list of the odd numbers from 1 to 20
# use a for loop to print each number

odd_nums = list(range(1, 20, 2))
for odd_num in odd_nums: # print individual numbers one at a time
    print(odd_num)
print()

# solution 2

odd_nums = list(range(1, 20, 2))
print(odd_nums) # prints in list format