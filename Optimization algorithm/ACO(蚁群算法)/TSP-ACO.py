import numpy as np

class AntColonyOptimization:
    def __init__(self, distance_matrix, n_ants, n_best, n_iterations, decay, alpha=1, beta=2):
        self.distance_matrix = distance_matrix  # 距离矩阵
        self.pheromone = np.ones(self.distance_matrix.shape) / len(distance_matrix)  # 初始化信息素矩阵
        self.all_inds = range(len(distance_matrix))  # 所有城市的索引
        self.n_ants = n_ants  # 蚂蚁数量
        self.n_best = n_best  # 选择前 n_best 个最短路径的蚂蚁
        self.n_iterations = n_iterations  # 最大迭代次数
        self.decay = decay  # 信息素挥发因子
        self.alpha = alpha  # 信息素重要性因子
        self.beta = beta  # 启发因子重要性因子

    def run(self):
        shortest_path = None  # 当前迭代中的最短路径
        all_time_shortest_path = ("placeholder", np.inf)  # 全局最短路径
        for i in range(self.n_iterations):
            all_paths = self.gen_all_paths()  # 生成所有蚂蚁的路径
            self.spread_pheromone(all_paths, self.n_best, shortest_path=shortest_path)  # 更新信息素
            shortest_path = min(all_paths, key=lambda x: x[1])  # 找到当前迭代中的最短路径
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path  # 更新全局最短路径
            self.pheromone *= self.decay  # 挥发信息素
        return all_time_shortest_path

    def spread_pheromone(self, all_paths, n_best, shortest_path):
        sorted_paths = sorted(all_paths, key=lambda x: x[1])  # 按路径长度排序
        for path, dist in sorted_paths[:n_best]:  # 选择前 n_best 个最短路径
            for move in path:
                self.pheromone[move] += 1.0 / self.distance_matrix[move]  # 增加信息素

    def gen_path_dist(self, path):
        total_dist = 0
        for ele in path:
            total_dist += self.distance_matrix[ele]  # 计算路径总长度
        return total_dist

    def gen_all_paths(self):
        all_paths = []
        for i in range(self.n_ants):
            path = self.gen_path(0)  # 生成路径
            all_paths.append((path, self.gen_path_dist(path)))  # 添加路径和路径长度
        return all_paths

    def gen_path(self, start):
        path = []
        visited = set()  # 已访问的城市集合
        visited.add(start)
        prev = start
        for i in range(len(self.distance_matrix) - 1):
            move = self.pick_move(self.pheromone[prev], self.distance_matrix[prev], visited)  # 选择下一个城市
            path.append((prev, move))
            prev = move
            visited.add(move)
        path.append((prev, start))  # 回到起点    
        return path

    def pick_move(self, pheromone, dist, visited):
        pheromone = np.copy(pheromone)
        pheromone[list(visited)] = 0  # 已访问城市的信息素设为 0

        row = pheromone ** self.alpha * ((1.0 / dist) ** self.beta)  # 计算概率

        norm_row = row / row.sum()  # 归一化概率
        move = np.random.choice(self.all_inds, 1, p=norm_row)[0]  # 按概率选择下一个城市
        return move

# 示例使用
distance_matrix = np.array([[np.inf, 2, 2, 5, 7],
                            [2, np.inf, 4, 8, 2],
                            [2, 4, np.inf, 1, 3],
                            [5, 8, 1, np.inf, 2],
                            [7, 2, 3, 2, np.inf]])

aco = AntColonyOptimization(distance_matrix, 10, 5, 100, 0.95, alpha=1, beta=2)
shortest_path, total_distance = aco.run()
formatted_path = [(int(start), int(end)) for start, end in shortest_path]
print(f"最短路径: {formatted_path}, 总距离: {total_distance}")

