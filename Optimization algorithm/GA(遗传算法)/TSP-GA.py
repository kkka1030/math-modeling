import random

# 城市之间的距离矩阵
distances = [
    [0, 2, 9, 10, 1],
    [2, 0, 6, 4, 3],
    [9, 6, 0, 8, 5],
    [10, 4, 8, 0, 7],
    [1, 3, 5, 7, 0]
]

# 初始化种群
def initialize_population(pop_size, num_cities):
    population = []
    for _ in range(pop_size):
        route = list(range(num_cities))
        random.shuffle(route)
        population.append(route)
    return population

# 计算路线的总距离
def calculate_total_distance(route):
    total_distance = 0
    for i in range(len(route)):
        total_distance += distances[route[i]][route[(i + 1) % len(route)]]
    return total_distance

# 评估适应度
def evaluate_population(population):
    fitness = []
    for route in population:
        total_distance = calculate_total_distance(route)
        fitness.append(1 / total_distance)
    return fitness

# 选择操作（轮盘赌选择）
def select_parents(population, fitness):
    total_fitness = sum(fitness)
    probabilities = [f / total_fitness for f in fitness]
    parents = random.choices(population, weights=probabilities, k=len(population))
    return parents

# 交叉操作（部分映射交叉）
def pmx(parent1, parent2):
    size = len(parent1)
    crossover_points=sorted(random.sample(range(size), 2))
    child1 = [None] * size

    # Copy the segment from parent1 to child1 and parent2 to child2
    for i in range(crossover_points[0], crossover_points[1]):
        child1[i] = parent1[i]
        

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
    

    return child1

# 变异操作（交换两个城市）
def mutate(route, mutation_rate):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]

# 遗传算法主循环
def genetic_algorithm(pop_size, num_cities, generations, mutation_rate):
    population = initialize_population(pop_size, num_cities)
    for generation in range(generations):
        fitness = evaluate_population(population)
        parents = select_parents(population, fitness)
        population = [pmx(parents[i], parents[(i + 1) % len(parents)]) for i in range(len(parents))]
        for route in population:
            mutate(route, mutation_rate)
    best_route = min(population, key=calculate_total_distance)
    return best_route, calculate_total_distance(best_route)

# 参数设置
pop_size = 10
num_cities = 5
generations = 100
mutation_rate = 0.1

best_route, best_distance = genetic_algorithm(pop_size, num_cities, generations, mutation_rate)
print("最佳路线:", best_route)
print("最短距离:", best_distance)
