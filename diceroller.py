import random

start = input('Do you want to roll the dice ? Type Yes to start ')


def roll():
    number = random.randrange(1, 6)
    print('You got ' + str(number))


if start == 'yes':
    print('You started rolling the dice')
    roll()
else:
    exit()
