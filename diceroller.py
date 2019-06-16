import random

statistics = list()

print('Welcome to Dice Rolling Simulator v1.5')
start = input('Do you want to roll the dice ? Type Yes to start ')


def stats():
    print('Here are the stats !')
    # roll count
    # mean
    sum_stats = sum(statistics)
    len_stats = len(statistics)
    mean = sum_stats/len_stats
    print('mean: ' + str(mean))
    # most common number
    # least common number


def roll():
    print('You started rolling the dice')
    number = random.randrange(1, 6)
    print('You got ' + str(number))
    statistics.append(number)
    reroll = input('Would you like to reroll ? ')
    while reroll == 'yes' or reroll == 'y':
        roll()
    else:
        stats_ask = input(
            'Type stats to see all your result or type something else to end the game ')
        if stats_ask == 'stats':
            stats()
        print('Thank you for playing !')
        exit()


if start == 'yes':
    roll()

# Stats
