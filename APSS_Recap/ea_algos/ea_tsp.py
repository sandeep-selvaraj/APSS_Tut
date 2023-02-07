import random
import numpy as np


def create_random_individual(cities):
    individual = list(range(cities))
    random.shuffle(individual)
    return individual


def evaluate_fitness(individual, distances):
    fitness = 0
    for i in range(len(individual) - 1):
        city_from = individual[i]
        city_to = individual[i + 1]
        fitness += distances[city_from][city_to]
    return fitness


def mutation(individual, mutation_prob):
    mutated_individual = list(individual)
    for i in range(len(individual)):
        if random.random() < mutation_prob:
            mutated_individual[i] = random.randint(0, len(individual) - 1)
    return mutated_individual


def recombination(individual_1, individual_2, recombination_prob):
    child = [-1] * len(individual_1)
    if random.random() < recombination_prob:
        start = random.randint(0, len(individual_1) - 1)
        end = random.randint(0, len(individual_1) - 1)
        if start > end:
            start, end = end, start
        for i in range(start, end + 1):
            child[i] = individual_1[i]
        for i in range(len(individual_2)):
            if individual_2[i] not in child:
                for j in range(len(child)):
                    if child[j] == -1:
                        child[j] = individual_2[i]
                        break
    else:
        child = individual_1
    return child

def evolutionary_algorithm(cities, distances, population_size, generation_size, mutation_prob, recombination_prob):
    population = [create_random_individual(cities) for _ in range(population_size)]
    for generation in range(generation_size):
        fitness = [evaluate_fitness(individual, distances) for individual in population]
        best_index = np.argmin(fitness)
        best_individual = population[best_index]
        new_population = []
        while len(new_population) < population_size:
            individual_1 = random.choice(population)
            individual_2 = random.choice(population)
            child = recombination(individual_1, individual_2, recombination_prob)
            mutated_child = mutation(child, mutation_prob)
            new_population.append(mutated_child)
        population = new_population
    return best_individual

