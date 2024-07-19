import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义 3 维 Rosenbrock 函数
def rosenbrock_3d(x, y, z):
    a = 1
    b = 100
    c = 100
    return (a - x)**2 + b * (y - x**2)**2 + c * (z - y**2)**2

# 创建网格
x = np.linspace(-2, 2, 50)
y = np.linspace(-1, 3, 50)
z = np.linspace(-1, 3, 50)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
W = rosenbrock_3d(X, Y, Z)

# 创建 3D 图形
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制散点图，使用颜色表示函数值
scatter = ax.scatter(X.flatten(), Y.flatten(), Z.flatten(), c=W.flatten(), cmap='viridis', alpha=0.5)

# 添加颜色条
fig.colorbar(scatter, ax=ax, shrink=0.5, aspect=5)

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Rosenbrock Function')

plt.show()


