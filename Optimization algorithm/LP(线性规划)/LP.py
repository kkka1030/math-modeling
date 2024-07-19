from scipy.optimize import linprog

# 定义目标函数的系数
c = [-3, -2]

# 定义不等式约束矩阵和向量
A = [[1, 0], [0, 1], [4, 2]]
b = [40, 60, 180]

# 定义变量的界
x0_bounds = (0, None)
x1_bounds = (0, None)

# 求解线性规划问题
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# 输出结果
print("最佳生产数量 (产品A, 产品B):", result.x)
print("最大化的利润:", -result.fun)
