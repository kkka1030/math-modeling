import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import griddata
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams['font.sans-serif'] = ['SimHei']

# Excel文件路径
path = r'C:\\Users\\31019\Desktop\\mathematical modeling\\问题B\\附件.xlsx'

df = pd.read_excel(path)
x = np.array(df.iloc[0][2:], dtype="float64")

y = []
for i in range(1, df.shape[0]):
    y.append(df.iloc[i][1])
y = np.array(y, dtype="float64")

# 乘以1852
x = x * 1852
y = y * 1852

z = []
for i in range(1, df.shape[0]):
    z.append(200-df.iloc[i][2:])
z = np.array(z, dtype="float64")
'''''
print(f"x: {x[:5]}")
print(f"y: {y[:5]}")
print(f"z: {z[0][0]}")
'''
# 将数据转换为1D数组
points = np.array([(xi, yi) for yi in y for xi in x])
values = z.flatten()
'''''
print(f"Number of points: {len(points)}")
print(f"Number of values: {len(values)}")
'''''
# 创建插值网格
grid_x, grid_y = np.mgrid[x.min():x.max():100j, y.min():y.max():100j]

# 进行三次样条插值
grid_z = griddata(points, values, (grid_x, grid_y), method='cubic')

# 绘制三维曲面图
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(grid_x, grid_y, grid_z, cmap='viridis')

# 添加颜色条
fig.colorbar(surf)

# 设置标签
ax.set_xlabel('横向坐标/NM')
ax.set_ylabel('纵向坐标/NM')
ax.set_zlabel('海水深度/m')

plt.show()
