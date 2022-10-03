"""
    File contains all constant variables that are
    used throughout the program.

    Feel free to tweak these values for your needs.
"""
from math import comb

# Number of queens on the board
N = 5

# Maximum number of generations (to avoid infinite loop)
MAX_GENERATIONS = 1000

# Max number of non-attacking queens is just a number of combinations of number of queens with length 2
MAX_NON_ATTACKING = comb(N, 2)

# Probability for mutating a Chromosome
MUTATION_PROBABILITY = 0.06

# Population size
POPULATION_SIZE = 4
