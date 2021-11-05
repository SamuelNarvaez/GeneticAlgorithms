import numpy as np
import math
import Chromosome
import FitnessFunctions
import itertools

class Generation:
    def __init__(self,generation=0,n=200,length = 8, range = 8, population=None):
        self.generation=generation
        self.length=length
        self.range=range
        self.selection = None
        self.size = n
        self.selectionsize = int(1+np.sqrt(1+8*self.size)/2)

        if population is None:
            self.population = np.array([])
            for i in range n:
                np.append(self.population, Chromosome(self.length,self.range))
        else:
            self.population = population

    def selection(self,fitness):
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
            np.append(fitnesses,chrom.fitness(fitness))
        sortindices = np.argsort(fitnesses)
        self.selection = self.population[sortindices[:self.selectionsize]

    def crossover(self, mask, newGenes):
      ''' arguments:
        selected population (array) - result of selection on self.population
        mask (string) - what crossover mask to use
        newGenes (float) - percent of population that should be randomly generated examples
      returns:
        result (array)

        add {newGenes}% random examples to {selected population},
        compute the crossover for every possible pairing of chromosomes in the population,
        return the results of the crossover
        '''
        selected = self.selection
        size = selected.shape[0]
        newGenes = math.floor(size/(1-newGenes)) - size #convert percent to number of new samples
        for i in range(newGenes):
            np.append(selected,Chromosome(self.length,self.range)) #generate new random examples for genetic diversity
        nextGeneration = np.array([])
        for pair in itertools.combinations(selected,2):
            np.append(nextGeneration,pair[0].crossover(pair[1]))

        return Generation(self.generation+1,self.size,self.length,self.range,population=nextGeneration)
