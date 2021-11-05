import numpy as np

class FitnessFunction:
    """ 
    attributes:
        fitness_function (string)
    """

    def __init__(self, fitness_function):
        self.fitness_function = fitness_function


    def count_notes(self, chromosome):
        num_notes = np.count_nonzero(chromosome)
        return num_notes
        

    def calc_fitness(self, chromosome):
        if self.fitness_function == "count_notes":
            return (self.count_notes(chromosome))

    