# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from GeneticAlgorithm import GeneticAlgorithm


class Product:
    def __init__(self, name, space, price):
        self.name = name
        self.space = space
        self.price = price


if __name__ == '__main__':
    products_list = [Product('Refrigerator A', 0.751, 999.90), Product('Cell phone', 0.00000899, 2911.12),
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
    population_size = 20
    mutation_probability = 0.01
    number_of_generation = 100
    ga = GeneticAlgorithm(population_size)
    result = ga.solve(mutation_probability, number_of_generation, spaces, prices, limit)
    ga.visualize_solutions(number_of_generation)
    print(result)
    for i in range(len(products_list)):
        if result[i] != '1':
            continue
        print("Name: ", products_list[i].name, " - Price: ", products_list[i].price)
