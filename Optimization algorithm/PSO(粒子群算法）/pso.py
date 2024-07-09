import numpy as np

# Rosenbrock函数
def rosenbrock(x, y):
    return (1 - x)**2 + 100 * (y - x**2)**2

# 参数初始化
w = 0.5
c1 = 1.5
c2 = 1.5
N = 30
T = 100
x_bound = [-10, 10]
y_bound = [-10, 10]

# 粒子位置和速度初始化
particles = np.random.rand(N, 2) * (x_bound[1] - x_bound[0]) + x_bound[0]
velocities = np.zeros((N, 2))

# 记录个体极值和全局极值
pBest = particles.copy()
gBest = particles[np.argmin([rosenbrock(p[0], p[1]) for p in particles])]

# 迭代更新
for t in range(T):
    for i in range(N):
        fitness = rosenbrock(particles[i, 0], particles[i, 1])
        if fitness < rosenbrock(pBest[i, 0], pBest[i, 1]):
            pBest[i] = particles[i]
        if fitness < rosenbrock(gBest[0], gBest[1]):
            gBest = particles[i]
    
    for i in range(N):
        r1, r2 = np.random.rand(), np.random.rand()
        velocities[i] = (w * velocities[i] 
                         + c1 * r1 * (pBest[i] - particles[i])
                         + c2 * r2 * (gBest - particles[i]))
        particles[i] += velocities[i]

# 输出最优解
print("最佳位置:", gBest)
print("最小值:", rosenbrock(gBest[0], gBest[1]))