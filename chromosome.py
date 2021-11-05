import numpy as np
from fitness import FitnessFunction
class Chromosome:
    """
    attributes:
    length (int)
    note_range (int)
    genotype (array)
    generation (int)
    fitness (float)
    """

    def __init__(self, n, note_range = 8, gen = 0,  sequence=[]):
        self.length = n
        self.note_range = note_range
        self.generation = gen

        """
        arguments:
            n(int) - length of chromosome array
            sequence (optional) - if None, randomly generate array of size {length}
            generation (optional) - if None, set to 0
        returns;
            new Chromosome with {genotype}=={genotype}
        """

        # assign the genotype to the chromosome if the input is of the correct length
        if len(sequence) == n:
            self.genotype = sequence
        else:
            self.genotype = np.random.randint(0, high = note_range, size = n)


            

    def crossover(parent1, parent2, mask):
        """
        arguments:
            parent1 (chromosome)
            parent2 (chromosome)
            mask (string) - the binary crossover mask 

        returns:
            offspring (list of chromosomes) - result of crossover
        """

        inv_mask = 1 - mask
        offspring = mask*parent1 + inv_mask*parent2

        return offspring
        
    def mutate(chromosome, note_range = 8, prob = 0):
        """
        arguments:
            chromosome (chromosome)
            prob (float)
        returns:
            new chromosome, which might be mutated according to prob
        """

        n = len(chromosome)

        # Which positions to mutate?
        to_mutate = np.random.choice([0, 1], size = n, p = [1-prob, prob])

        # What are those values mutated to?
        mutations = np.random.randint(0, high = note_range, size = n)*to_mutate

        # Add the mutations to the original chromosome
        mutated = (1-to_mutate)*chromosome + to_mutate*mutations

        return mutated


    def fitness_calculate(self, fitness_function):
        """
        arguments:
            fitness function
        returns:
            None, assigns result of fitness function to self.fitness
        """
        f = FitnessFunction(fitness_function)
        self.fitness = f.calc_fitness(self.genotype)
        return None
