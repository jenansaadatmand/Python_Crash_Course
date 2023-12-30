# Exercise 8-16 Imports: using a program you wrote that has one function in it,
# Store that function in a separate file
# Import the function into your main program file, 
# and call the function using each of these approcahes:
# Import module_name
# From module_name import function_name
# From module_name import function_name as fn
# Import module_name as mn
# From module_name import *


# Import module_name

import build_profile_function
user_profile = build_profile_function.build_profile('jenan', 'saadatmand', age = 47, hair = 'black', eyes = 'brown', hobby = 'motorbiking')
print(user_profile)
print("\n")

# From module_name import function_name
from build_profile_function import build_profile
user_profile = build_profile('jenan', 'saadatmand', age = 47, hair = 'black', eyes = 'brown', hobby = 'motorbiking')
print(user_profile)
print("\n")

# From module_name import function_name as fn
from build_profile_function import build_profile as bp
user_profile = bp('jenan', 'saadatmand', age = 47, hair = 'black', eyes = 'brown', hobby = 'motorbiking')
print(user_profile)
print("\n")

# import module_name as mn
import build_profile_function as bpf
user_profile = bpf.build_profile('jenan', 'saadatmand', age = 47, hair = 'black', eyes = 'brown', hobby = 'motorbiking')
print(user_profile)
print("\n")

# from module_name import *
from build_profile_function import *
user_profile = build_profile('jenan', 'saadatmand', age = 47, hair = 'black', eyes = 'brown', hobby = 'motorbiking')
print(user_profile)
print("\n")

