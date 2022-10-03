"""
    File contains all the functions needed to
    solve N-queen genetic problem
"""
import random
from itertools import combinations

from constants import N
from utils import attacks


def generate_chromosomes() -> list[int]:
    """ Randomly generate a list of N random values, each from 1 to N """
    return [random.randint(1, N) for _ in range(N)]


def fitness(queens: list[int]) -> int:
    """ Counts number of queen pairs that do not attack each other """
    non_attacking_pairs = 0

    # queens list's values represents rows and indexes represent columns
    # Reformat it so that each value in list has row and column
    queens = [(col, row) for col, row in enumerate(queens)]

    for pair in combinations(queens, 2):
        if not attacks(*pair):
            non_attacking_pairs += 1

    return non_attacking_pairs


def crossover(queens1: list[int], queens2: list[int]) -> tuple[list[int], list[int]]:
    """
        Randomly select a point at which two chromosomes will be sliced and flipped

        Example:
             queens1 = [1, 2, 3, 4, 5]
             queens2 = [5, 4, 3, 2, 1]

             Suppose we randomly selected 3, it means that

             [1, 2, 3] | [4, 5]
             [5, 4, 3] | [2, 1]

             Function will return

             [1, 2, 3, 2, 1] and [5, 4, 3, 4, 5]
    """
    assert len(queens1) == len(queens2), 'Hey, lists must be the same in length!'

    random_point = random.randint(1, len(queens1) - 1)  # [1, 4]

    return (
        queens1[:random_point] + queens2[random_point:],
        queens2[:random_point] + queens1[random_point:]
    )


def mutate(queens) -> None:
    """ Randomly change one of values """
    index_of_value_to_change = random.randint(0, N - 1)
    queens[index_of_value_to_change] = random.randint(1, N)