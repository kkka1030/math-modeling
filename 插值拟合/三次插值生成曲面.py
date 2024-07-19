import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# 输入数据
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 2, 3, 4])
'''''
z = np.array([
    [5, 3, 3, 2, 5],
    [3, 3, 2, 5, 6],
    [3, 2, 5, 6, 7],
    [2, 5, 6, 6, 5],
    [5, 6, 7, 5, 4]
])
'''''
z = np.random.rand(5, 5)
# 创建网格
x_grid, y_grid = np.meshgrid(x, y)

# 将输入数据转换为一维数组
x_flat = x_grid.flatten()
y_flat = y_grid.flatten()
z_flat = z.flatten()

# 定义新的网格点进行插值
x_new = np.linspace(0, 4, 100)
y_new = np.linspace(0, 4, 100)
x_new_grid, y_new_grid = np.meshgrid(x_new, y_new)

# 使用三次样条插值生成曲面
z_new = griddata((x_flat, y_flat), z_flat, (x_new_grid, y_new_grid), method='cubic')

# 可视化结果
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_new_grid, y_new_grid, z_new, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Cubic Spline Interpolation Surface')

plt.show()






