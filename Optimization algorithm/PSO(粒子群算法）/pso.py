import numpy as np
import matplotlib.pyplot as plt
from pyswarms.single import GlobalBestPSO
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文
# 定义目标函数
def objective_function(x):
    return (x[:,0]-3)**2+(x[:,1]-4)**2

# 定义约束条件
def constraint(x):
    constraints = [
        x[:,0] + x[:,1] >= 5  # 线性约束：x0 + x1 >= 5
    ]
    return np.all(constraints, axis=0)

# 惩罚函数
def penalized_objective_function(x):
    penalty = np.zeros((x.shape[0],1))
    penalty[constraint(x)]=500
    
    return objective_function(x) + penalty.reshape(-1)

# 修复函数
def repair(x):
    if x[0] + x[1] < 5:
        x[1] = 5 - x[0]
    
    return x

# 粒子群优化参数
n_particles = 1000
n_dimensions = 2  # 假设问题有4个变量
options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}

# 初始化粒子的位置和边界
lower_bound = np.array([0, 0])
upper_bound = np.array([5, 5])

# 使用GlobalBestPSO进行优化
optimizer = GlobalBestPSO(n_particles=n_particles, dimensions=n_dimensions, options=options, bounds=(lower_bound, upper_bound))
best_cost, best_position = optimizer.optimize(penalized_objective_function, iters=1000)

#修复最佳位置，使其满足约束条件
#best_position = repair(best_position)

print('Best position:', best_position)
print('Best cost:', best_cost)

# 可视化结果
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(optimizer.cost_history)
ax.set_title("目标函数（-利润）变化曲线")
ax.set_xlabel("迭代次数")
ax.set_ylabel("成本")
plt.show()






