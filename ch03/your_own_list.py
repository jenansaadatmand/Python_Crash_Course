# Think of your favourite mode of transportation, such as a motorcycle or a car,
# And make a list that stores several examples
# Use your list to print a series of statements about these items, such as "I would like to own a Honda motorcycle"


# Solution 1:

mode_transport = ['motorcycle', 'car', 'bus', 'train', 'aeroplane', 'ship']
print(f'I would like to own a Honda {mode_transport[0].title()}')
print(f'I would like to own a Toyota {mode_transport[1].title()}')
print(f'I would like to own a public {mode_transport[2].title()}')
print(f'I would like to own a public {mode_transport[3].title()}')
print(f'I would like to own a flying {mode_transport[4].title()}')
print(f'I would like to own a crusing {mode_transport[5].title()}')
print()


# Solution 2:

mode_transport = ['motorcycle', 'car', 'bus', 'train', 'aeroplane', 'ship']
msg = 'I would like to own a ' 
print(f'{msg}{mode_transport[0].title()}')
print(f'{msg}{mode_transport[1].title()}')
print(f'{msg}{mode_transport[2].title()}')
print(f'{msg}{mode_transport[3].title()}')
print(f'{msg}{mode_transport[4].title()}')
print(f'{msg}{mode_transport[5].title()}')
