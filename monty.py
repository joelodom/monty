'''Simulate the Monty Hall problem.'''

import random  # good enough for this simulation

ITERATIONS = 10000
SWITCH = True  # change this to false if you don't want the player to switch

wins = 0  # the number of cars won

for i in range(ITERATIONS):

    # initialize the iteration
    car = random.randint(0, 2)

    # the player chooses at random
    choice = random.randint(0, 2)

    # It turns out that making a revelation here only collapses the algorithm
    # to this, making the outcome obvious!  There is no need even to run this
    # simulation!

    # switch if configured to do so
    if choice == car:
        if not SWITCH:
            wins += 1
    elif SWITCH:
        wins += 1

print(f'Fraction of wins: {wins / ITERATIONS}')
