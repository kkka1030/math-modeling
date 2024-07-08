import random

def pmx(parent1, parent2, crossover_points):
    size = len(parent1)
    child1, child2 = [None] * size, [None] * size

    # Copy the segment from parent1 to child1 and parent2 to child2
    for i in range(crossover_points[0], crossover_points[1]):
        child1[i] = parent1[i]
        child2[i] = parent2[i]

    def map_gene(child, other_parent, segment_start, segment_end):
        for i in range(segment_start, segment_end):
            if child[i] is None:
                gene = other_parent[i]
                while gene in child:
                    gene = other_parent[child.index(gene)]
                child[i] = gene

    # Mapping the genes
    map_gene(child1, parent2, 0, crossover_points[0])
    map_gene(child1, parent2, crossover_points[1], size)
    map_gene(child2, parent1, 0, crossover_points[0])
    map_gene(child2, parent1, crossover_points[1], size)

    return child1, child2

# Example usage:
parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
parent2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
crossover_points = (3, 7)  # These should be selected randomly, example used here for clarity

child1, child2 = pmx(parent1, parent2, crossover_points)
print("Parent 1: ", parent1)
print("Parent 2: ", parent2)
print("Child 1:  ", child1)
print("Child 2:  ", child2)

