# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# from turtle import forward, left
from Individual import Individual
from GeneticAlgorithm import GeneticAlgorithm


class Product:
    def __init__(self, name, space, price):
        self.name = name
        self.space = space
        self.price = price


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # for i in range(1, 100):
    #    forward(2 * i)
    #    left(90)
    # p1 = Product('Refrigerator A', 0.75, 999.9)
    # p2 = Product('Cell phone', 0.00000899, 2199.12)
    # print(f'The attribute of the class Product, {p1.name}')
    products_list = [Product('Refrigerator A', 0.751, 999.90), Product('Cell phone', 0.00000899, 2199.12),
                     Product('TV 55', 0.400, 4346.99), Product("TV 50' ", 0.290, 3999.90),
                     Product("TV 42' ", 0.200, 2999.00), Product("Notebook A", 0.00350, 2499.90),
                     Product("Ventilator", 0.496, 199.90), Product("Microwave A", 0.0424, 308.66),
                     Product("Microwave B", 0.0544, 429.90), Product("Microwave C", 0.0319, 299.29),
                     Product("Refrigerator B", 0.635, 849.00), Product("Refrigerator C", 0.870, 1199.89),
                     Product("Notebook B", 0.498, 1999.90), Product("Notebook C", 0.527, 3999.00)]
    spaces = []
    prices = []
    names = []
    for product in products_list:
        print(product.name, '-', product.space, '-', product.price)
        spaces.append(product.space)
        names.append(product.name)
        prices.append(product.price)

    limit = 3  # Maximum capacity of the Truck
    individual1 = Individual(spaces, prices, limit)
    print('Spaces: ', individual1.spaces)
    print('Prices: ', individual1.prices)
    print('Individual1 Chromosome: ', individual1.chromosome)

    for i in range(len(products_list)):
        if individual1.chromosome[i] == '1':
            print(products_list[i].name, '-', products_list[i].space, '-', products_list[i].price)

    print('Individual1 fitness value: ', individual1.fitness())

    print('Score: ', individual1.score_evaluation)
    print('Used Space: ', individual1.used_space)

    individual2 = Individual(spaces, prices, limit)
    # print('Spaces: ', individual2.spaces)
    # print('Prices: ', individual2.prices)
    print('Individual2 Chromosome: ', individual2.chromosome)

    for i in range(len(products_list)):
        if individual2.chromosome[i] == '1':
            print(products_list[i].name, '-', products_list[i].space, '-', products_list[i].price)

    print('Individual2 fitness value: ', individual2.fitness())
    print('Score: ', individual2.score_evaluation)
    print('Used Space: ', individual2.used_space)

    children = individual1.crossover(individual2)
    children[0].fitness()
    children[1].fitness()
    print('children[0] Score: ', children[0].score_evaluation)
    print('children[0] Used Space: ', children[0].used_space)
    print('children[1] Score: ', children[1].score_evaluation)
    print('children[1] Used Space: ', children[1].used_space)

    individual1.mutation(0.05)

    population_size = 20
    ga = GeneticAlgorithm(population_size)
    ga.initialize_population(spaces, prices, limit)

    # print(ga.population[0].chromosome)

    for individual in ga.population:
        individual.fitness()

    ga.order_population()
    ga.best_individual(ga.population[0])

    for i in range(ga.population_size):
        print('individual', i, ' fitness: ', ga.population[i].score_evaluation)

    print('Best solution: ', ga.best_solution.score_evaluation)

    sum_eval = ga.sum_evaluations()
    print("Sum of evaluations: ", sum_eval)

    parent1 = ga.select_parent(sum_eval)
    parent2 = ga.select_parent(sum_eval)