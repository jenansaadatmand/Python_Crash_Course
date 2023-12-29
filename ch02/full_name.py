# Using variables in string , using f-string, f for format
# python replaces the name of any variable in braces with its value
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
# Use f-string to compose complete messages using information associated with a variable
print(f"Hello, {full_name.title() } !")

# also you can use f-string to compose a message, then assign the entire message to a variable

print()
message  = f"Hello, {full_name.title()} !"
print(message)