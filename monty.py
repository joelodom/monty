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

    # "reveal" a goat (not the fastest algorithm, but easy to understand)
    revealed = -1
    while revealed != choice and revealed != car:
        revealed = random.randint(0, 2)

    # switch if configured to do so
    if SWITCH:
        choice = 3 - revealed - choice  # it works, trust me

    # tally
    if choice == car:
        wins += 1

print(f'Fraction of wins: {wins / ITERATIONS}')
