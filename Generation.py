class Generation:
  attributes:
    number (int) - which generation is it?
    population (array) - all chromosomes in the Generation
  methods:
    __init__
      arguments:
        n (int) - initial population size
      returns:
        a new generation object, populated with n randomly generated chromosomes
    selection
      arguments:
        population (array)
        ratio (float)
        fitness (function)
      returns:
        the top {ratio}% of {population} according to {fitness}
    crossover
      arguments:
        selected population (array) - result of selection on self.population
        method (string) - what crossover method to use
        newGenes (float) - percent of population that should be randomly generated examples
      returns:
        add {newGenes}% random examples to {selected population},
        compute the crossover for every possible pairing of chromosomes in the population,
        return the results of the crossover
