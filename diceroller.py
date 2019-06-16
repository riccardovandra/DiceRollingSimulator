import random

statistics = list()

print('Welcome to Dice Rolling Simulator 1.0')
start = input('Do you want to roll the dice ? Type Yes to start ')


def stats():
    # roll count
    # mean
    # most common number
    # least common number
    print('Here are the stats')


def roll():
    print('You started rolling the dice')
    number = random.randrange(1, 6)
    print('You got ' + str(number))
    statistics.append(number)
    print(statistics)
    reroll = input('Would you like to reroll ? ')
    while reroll == 'yes' or reroll == 'y':
        roll()
    else:
        print('Thank you for playing !')
        exit()


if start == 'yes':
    roll()

# Stats
