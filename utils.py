import random

from constants import N


def attacks(queen_position_1: tuple[int, int], queen_position_2: tuple[int, int]) -> bool:
    """ Determines whether queens attack each other or not """
    col_1, row_1 = queen_position_1
    col_2, row_2 = queen_position_2

    results = (
        row_1 == row_2,  # Same row (True/False)
        col_1 == col_2,  # Same col (True/False)
        abs(row_1 - row_2) == abs(col_1 - col_2)  # Diagonally attacks (True/False)
    )

    return any(results)  # Returns True if any of the results is True


def print_queens_on_board(queens: list[int]):
    """ Function is quite messy, just trust that it works as expected :D """
    separator = '-' * (4 * N + 1)

    rows = [
        [] for _ in range(N)
    ]

    for target_row in queens:
        for j in range(N):
            rows[j].append(
                ' Q ' if target_row == j + 1 else '   '
            )

    print(separator)
    for item in reversed(rows):
        row = '|'.join(item)
        print(f'|{row}|')
        print(separator)


def weighted_choice(population_with_fitness_values: list[tuple[list[int], int]], total):  # From https://stackoverflow.com/a/3679747/14099193
    """ Randomly choose based on weights (fitness values) """
    r = random.uniform(0, total)
    upto = 0

    for queens, fitness_value in population_with_fitness_values:
        if upto + fitness_value >= r:
            return queens

        upto += fitness_value

    assert False, "Shouldn't get here"
