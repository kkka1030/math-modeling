import numpy as np
from scipy.optimize import differential_evolution, NonlinearConstraint

# 定义目标函数
def rosenbrock(x):
    return sum(100.0 * (x[1:] - x[:-1]**2.0)**2.0 + (1 - x[:-1])**2.0)

# 定义变量的边界
bounds = [(-10, 10), (-10, 10),(-10,10)]

# 定义非线性约束函数
def constraint1(x):
    return 1 - (x[0] + x[1])

def constraint2(x):
    return 1 - (x[0]**2 + x[1]**2)

#创建回调函数
def callback_func(xk, convergence):
    print(f"当前解: {xk}, 当前收敛度: {convergence}")

# 创建非线性约束对象
nonlinear_constraint1 = NonlinearConstraint(constraint1, -np.inf, 0)
nonlinear_constraint2 = NonlinearConstraint(constraint2, -np.inf, 0)

# 使用差分进化算法进行优化
result = differential_evolution(rosenbrock, bounds, constraints=[nonlinear_constraint1, nonlinear_constraint2],callback=callback_func)

# 输出优化结果
print('最优解:', result.x)
print('最优值:', result.fun)



