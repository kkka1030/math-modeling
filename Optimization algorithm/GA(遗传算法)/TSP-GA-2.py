import numpy as np
from scipy.optimize import differential_evolution

# 距离矩阵
distances = [
    [0, 2, 9, 10, 1],
    [2, 0, 6, 4, 3],
    [9, 6, 0, 8, 5],
    [10, 4, 8, 0, 7],
    [1, 3, 5, 7, 0]
]

# 定义TSP的目标函数
def total_distance(permutation):
    # 将连续值解码为离散排列
    perm = np.argsort(permutation)
    distance = 0
    for i in range(len(perm) - 1):
        distance += distances[perm[i]][perm[i + 1]]
    distance += distances[perm[-1]][perm[0]]  # 回到起点
    return distance

# 定义约束：所有值必须是整数
bounds = [(0, len(distances) - 1)] * len(distances)

# 使用differential_evolution解决TSP
result = differential_evolution(total_distance, bounds, strategy='best1bin', maxiter=1000, popsize=15, mutation=(0.5, 1), recombination=0.7, disp=True)

# 获取最优路径
optimal_permutation = result.x

# 将连续值解码为离散排列
optimal_route = np.argsort(optimal_permutation)

print("最优路径:", optimal_route)
print("最短距离:", total_distance(optimal_permutation))

