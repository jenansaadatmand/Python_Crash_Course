# If statement in a loop, writing conditional tests allowing to check any condition of interest
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print("\n")

# Another example
for i in cars:
    if i  == "toyota":
        print(i.upper())
    else:
        print(i.lower())
