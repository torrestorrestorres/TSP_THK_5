# Evolutionary Algorithm

# -------------------------------
# Representation: Route = List of integers associated with cities e.g. [0,1,2,3,4,5]

# Variation Operators:
#   Crossover:
#       Order 1 Crossover: Select a random section of the first parent, remove these cities from the second parent and insert them into the child
#   Mutation:
#       two_op_swap() function will randomly swap two cities in a route

# Fitness Evaluation: get_cost_of_route() function which adds up the distances between all cities in a route

# Selection Operators:
# µ = Parents
# λ = Offspring

# (µ + λ) - EA, Plus Selektion

# Parent Selection:
#       Tournament Selection, Selection of parents chosen at random and best parent returned
#       Get k random parents, select the best parent from the k parents
#       Repeat µ times to get µ parents

# Survivor Selection:
#       Fitness Proportional Selection, Selection of survivors based on their fitness
#       Give each individual a probability of being selected based on their fitness
#       Higher fitness = higher probability of being selected
#       Repeat µ times to get µ survivors


# -------------------------------

# Imports
import math
import random
import time


# -------------------------------


def get_cities(city_file):
    # Function to read in the cities from the file and store them in a list
    global read_cities
    file = open("data/" + city_file, "r")

    # A city is defined by a line with 3 numbers separated by spaces e.g. 1 288 149
    # The first number is the city number, the second is the x coordinate and the third is the y coordinate
    # The file ends with a line containing "EOF" and starts with a line containing "NODE_COORD_SECTION"
    cities = []

    read = False

    for x in file:
        if x == "NODE_COORD_SECTION\n":
            read = True
            continue
        if x == "EOF\n":
            break
        if read:  # If we are in the section of the file containing the cities
            city = x.split()
            cities.append((float(city[1]), float(city[2])))  # Add the city to the list of cities

    # Return the list of cities
    return cities


def get_distance(city1, city2):
    # Function to calculate the distance between two cities
    x1, y1 = city1
    x2, y2 = city2

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def get_cost_of_route(route, cities):
    # Function to calculate the cost of a route
    cost = 0

    # Loop through the cities in the route
    for i in range(len(route) - 1):
        # Add the distance between the current city and the next city in the route
        cost += get_distance(cities[route[i]], cities[route[i + 1]])

    # Add the distance between the last city in the route and the first city in the route
    cost += get_distance(cities[route[-1]], cities[route[0]])

    # Return the total cost of the route
    return cost


def two_opt_swap(route):
    # Function to perform a 2-opt swap on a route
    # Select two random indices in the route
    i, j = random.sample(range(len(route)), 2)

    # Swap the cities at these indices
    route[i], route[j] = route[j], route[i]

    # Return the new route
    return route


def order_one_crossover(parent1, parent2):
    # Function to perform order 1 crossover on two parent routes
    # Select a random section of the first parent route
    start = random.randint(0, len(parent1) - 1)
    end = random.randint(start, len(parent1) - 1)
    section = parent1[start:end]

    # Create a copy of the second parent route
    child = parent2.copy()

    # Remove the cities in the selected section from the child route
    for city in section:
        child.remove(city)

    # Insert the selected section into the child route
    for i in range(len(section)):
        child.insert(start + i, section[i])

    # Return the child route
    return child


def tournament_selection(population, tournament_size):
    # Function to perform tournament selection on the population
    parents = []

    # Repeat tournament selection to get the required number of parents
    for i in range(len(population)):
        # Select k random individuals from the population
        tournament = random.sample(population, tournament_size)

        # Get the best individual from the tournament
        best = min(tournament, key=lambda x: x[1])

        # Add the best individual to the list of parents
        parents.append(best)

    # Return the list of parents
    return parents


def fitness_proportional_selection(population, num_survivors):
    # Function to perform fitness proportional selection on the population
    survivors = []

    # Calculate the total fitness of the population
    total_fitness = sum([x[1] for x in population])

    # Calculate the probability of each individual being selected
    probabilities = [x[1] / total_fitness for x in population]

    # Repeat selection to get the required number of survivors
    for i in range(num_survivors):
        # Select an individual based on their probability
        survivor = random.choices(population, probabilities)[0]

        # Add the selected individual to the list of survivors
        survivors.append(survivor)

    # Return the list of survivors
    return survivors


def do_evolution(population, cities, tournament_size, mutation_rate):
    # Function to perform one generation of the evolutionary algorithm
    # Select parents from the population using tournament selection
    parents = tournament_selection(population, tournament_size)

    # Create offspring by performing crossover on the parents
    offspring = []
    for i in range(0, len(parents), 2):
        child1 = order_one_crossover(parents[i][0], parents[i + 1][0])
        child2 = order_one_crossover(parents[i + 1][0], parents[i][0])
        offspring.append((child1, get_cost_of_route(child1, cities)))
        offspring.append((child2, get_cost_of_route(child2, cities)))

    # Perform mutation on the offspring
    for i in range(len(offspring)):
        if random.random() < mutation_rate:
            offspring[i] = (two_opt_swap(offspring[i][0]), get_cost_of_route(offspring[i][0], cities))

    # Combine the parents and offspring
    combined_population = parents + offspring

    # Select survivors from the combined population using fitness proportional selection
    num_survivors = len(population)
    survivors = fitness_proportional_selection(combined_population, num_survivors)

    # Return the survivors
    return survivors


def main():
    start_time = time.time()

    # ------Variables------ #

    # cityfile = "a280.tsp"
    cityfile = "att48.tsp"

    # Read in the cities from the file
    cities = get_cities(cityfile)

    # Create the initial population
    population_size = 100

    # Set the number of generations
    num_generations = 10000

    # Set the tournament size
    tournament_size = 5

    # Set the mutation rate
    mutation_rate = 1 / len(cities)

    # --------------------- #

    population = []
    for i in range(population_size):
        route = list(range(len(cities)))
        random.shuffle(route)
        cost = get_cost_of_route(route, cities)
        population.append((route, cost))

    # Perform the evolutionary algorithm for the specified number of generations
    for i in range(num_generations):
        population = do_evolution(population, cities, tournament_size, mutation_rate)

        # Print the best route in the population
        best_route = min(population, key=lambda x: x[1])
        print("Generation", i + 1, "- Best Route:", best_route[0], "- Cost:", best_route[1])

    end_time = time.time()

    print("Time taken: ", end_time - start_time)

    # Print the best route in the population
    best_route = min(population, key=lambda x: x[1])
    print("Best Route:", best_route[0], "- Cost:", best_route[1])


main()
