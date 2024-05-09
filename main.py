# Evolutionary Algorithm
#
# -------------------------------
# Representation: Route = List of integers associated with cities e.g. [0,1,2,3,4,5]
# Fitness Evaluation: get_cost_of_route() function which adds up the distances between all cities in a route
# Recombination: Order 1 Crossover function which takes a random section of one route and inserts it into another route while keeping all elements unique
# Recombination Probability: 100% (Required)
# Mutation: two_op_swap() function will randomly swap two cities in a route
# Mutation Probability: Test: 20%, Actual: 50%
# Parent Selection: Tournament Selection, Selection of parents chosen at random and best parent returned
# Survivor Selection: Elitism Model, Offspring added to parent population, then culled based on fitness back to {population size}
# Selection Size: TEst = 10, Actual = 30
# Population Size: Test = 100, Actual = 200
# Initialisation: Create a list of length {population size} containing randomly generated routes. Repetitions are allowed.
# Termination: After 42 generations tested
#