import random

statistics = list()
rollcount = 0

print('Welcome to Dice Rolling Simulator v2')
start = input('Do you want to roll the dice ? Type Yes to start ')


def stats():
    most_common = list()
    print('Here are the stats !')
    # roll count
    print('Roll Count:', rollcount)
    # mean
    sum_stats = sum(statistics)
    len_stats = len(statistics)
    mean = sum_stats/len_stats
    print('mean:', mean)
    # get count
    for x in [1, 2, 3, 4, 5, 6]:
        count = statistics.count(x)
        most_common.append([x, count])
    # sort based on the number of times a number is rolled

    def sortSecond(val):
        return val[1]
    mc_sorted = sorted(most_common, key=sortSecond, reverse=True)
    # most common number
    print('most common number:', mc_sorted[0]
          [0], 'rolled', mc_sorted[0][1], 'times')
    # least common number
    print('least common number:',
          mc_sorted[-1][0], 'rolled', mc_sorted[-1][1], 'times')

    # counter stats
    print('Additional Stats')
    print('')
    for key, value in most_common:
        print(key, 'rolled', value, 'times')
    print(most_common)


def roll():
    global rollcount
    rollcount = rollcount + 1
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
