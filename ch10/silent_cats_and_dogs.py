# Silent cats and dogs: 
# Modify your except block in excersize 10-8 to fail silently if either file is missing

filenames = ['text_files/cats.txt', 'text_files/dogs.txt']
for filename in filenames:

    try:
        with open(filename, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else: 
        print(f"\nReading file: {filename}")
        print(contents)

# Remove one or both files from the same directory to check if an exception is handled
