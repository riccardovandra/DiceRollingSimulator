import random

print('Welcome to Dice Rolling Simulator 1.0')
start = input('Do you want to roll the dice ? Type Yes to start ')


def roll():
    print('You started rolling the dice')
    number = random.randrange(1, 6)
    print('You got ' + str(number))
    reroll = input('Would you like to reroll ? ')
    while reroll == 'yes':
        roll()
    else:
        print('Thank you for playing !')
        exit()


if start == 'yes':
    roll()
