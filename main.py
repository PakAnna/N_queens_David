"""
    This is a main script. It executes all needed routines
    to solve the N-queen genetic problem


    Steps for genetic algorithm:
        1) Chromosome design
        2) Initialization
        3) Fitness evaluation
        4) Selection
        5) Crossover
        6) Mutation
        7) Update generation
        8) Go back to 3)


    Some useful terminology:

        Gene = Queen at some specific position
        Chromosome = 5 queens (genes) each at specific position
        Population = Set of all Chromosomes at this point
        Fitness Function = Count number of pairs of non-attacking queens
        Crossover (Recombination) = Generate a new set of positions for 5 queens (Chromosome)
          based on two parents (also positions of queens)
        Mutation = Randomly alter one or more queen positions in some Chromosome
"""
import random

from constants import N, MAX_NON_ATTACKING, POPULATION_SIZE, MUTATION_PROBABILITY, MAX_GENERATIONS
from genetic_algorithm import generate_chromosomes, fitness, crossover, mutate
from utils import weighted_choice, print_queens_on_board


def genetic_function() -> tuple[int, list[int]] | None:
    """
        Main function. All the important stuff goes here.
        Returns (generation #, solution) if solution is found, None otherwise
    """
    # Step 1: We designed chromosomes to be a list of values, representing queens row position
    # [3, 2, 3, 4, 5] will look like
    # ---------------------
    # |   |   |   |   | Q |
    # ---------------------
    # |   |   |   | Q |   |
    # ---------------------
    # | Q |   | Q |   |   |
    # ---------------------
    # |   | Q |   |   |   |
    # ---------------------
    # |   |   |   |   |   |
    # ---------------------

    # Step 2: Randomly generate initial population
    population = [
        generate_chromosomes()
        for _ in range(POPULATION_SIZE)  # Generate POPULATION_SIZE random chromosomes
    ]
    generation = 1

    while True:
        if generation > MAX_GENERATIONS:
            break

        population_with_fitness_values = []
        overall_fitness = 0
        max_fitness = 0

        # Step 3: Fitness evaluation
        for chromosome in population:
            fitness_value = fitness(chromosome)

            max_fitness = max(max_fitness, fitness_value)
            overall_fitness += fitness_value

            population_with_fitness_values.append(
                (chromosome, fitness_value)
            )

            if fitness_value == MAX_NON_ATTACKING:
                return generation, chromosome  # Nobody is attacked, we are done

        print(f'Generation {generation: 3}, Max fitness value: {max_fitness}/{MAX_NON_ATTACKING}')

        new_population = []
        for _ in range(POPULATION_SIZE):  # Iterate POPULATION_SIZE times
            # Step 4: Selection (Pick mom and dad)
            parent1 = weighted_choice(population_with_fitness_values, total=overall_fitness)
            parent2 = weighted_choice(population_with_fitness_values, total=overall_fitness)

            # Step 5: Crossover (Reproduce)
            child1, child2 = crossover(queens1=parent1, queens2=parent2)
            # we will skip child2 so that population does not grow (納扎爾)

            # Step 6: Mutation
            if random.random() < MUTATION_PROBABILITY:
                mutate(child1)

            new_population.append(child1)

        # Step 7: Update generation
        population = new_population
        generation += 1


if __name__ == '__main__':  # A Python stuff... You may Google it, if you need
    result = genetic_function()

    if result is None:
        print(f'Could not find solution throughout {MAX_GENERATIONS}')
    else:
        generation, solution = result

        print(f'Solution found at {generation =}')
        print_queens_on_board(solution)
