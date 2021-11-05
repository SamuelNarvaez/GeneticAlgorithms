import numpy as np
import math
from chromosome import Chromosome
from fitness import FitnessFunction
import itertools

class Generation:
    def __init__(self,generation=0,n=200,length = 8, note_range = 8, population=None):
        self.generation=generation
        self.length=length
        self.note_range=note_range
        self.selected = None
        self.size = n
        self.selectionsize = int(1+np.sqrt(1+8*self.size)/2)

        if population is None:
            self.population = np.array([])
            for i in range(n):
                self.population = np.append(self.population, Chromosome(self.length,self.note_range))
        else:
            self.population = population

    def selection(self,fitness_function):
        '''
      arguments:
        self.population (array)
        ratio (float)
        fitness (function)
      returns:
        the top {ratio}% of {population} according to {fitness}
        '''
        fitnesses = np.array([])
        for chrom in self.population:
            fitnesses = np.append(fitnesses,chrom.fitness_calculate(fitness_function))
        sortindices = np.argsort(fitnesses)
        result = self.population[sortindices[:self.selectionsize]]
        self.selected = Generation(0,result.shape[0],self.length,self.note_range,population=result)

    def batch_crossover(self, mask, newGenes):
        ''' arguments:
        selected population (array) - result of selection on self.population
        mask (string) - what crossover mask to use
        newGenes (float) - percent of population that should be randomly generated examples
      returns:
        result (array)
        add {newGenes}% random examples to {selected population},
        compute the crossover for every possible pairing of chromosomes in the population,
        return the results of the crossover '''
        size = self.selected.size
        newGenes = math.floor(size/(1-newGenes)) - size #convert percent to number of new samples
        for i in range(newGenes):
            self.selected.population = np.append(self.selected.population,Chromosome(self.length,self.note_range)) #generate new random examples for genetic diversity
        nextGeneration = np.array([])
        for pair in itertools.combinations(self.selected.population,2):
            nextGeneration = np.append(nextGeneration,pair[0].crossover(pair[1],mask))

        return Generation(self.generation+1,self.size,self.length,self.note_range,population=nextGeneration)
