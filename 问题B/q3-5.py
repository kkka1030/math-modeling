import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def sin(a):
    return np.sin(np.radians(a))

def cos(a):
    return np.cos(np.radians(a))

def tan(a):
    return np.tan(np.radians(a))

def get_Wleft(D):
    return D*sin(theta/2)/sin(90-theta/2-alpha)

angle = 90
alpha = np.linspace(0.5, 10, 100)
theta = np.linspace(90, 150, 100)
x_d = 70
w = []

for i in alpha:
    for j in theta:
        w.append(x_d*sin(j/2)*(1/sin(90-j/2-i)+1/sin(90-j/2+i)))

print(w)
w = np.array(w).reshape(100, 100)
alpha, theta = np.meshgrid(alpha, theta)

# 创建三维图形对象和坐标轴
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制三维图形
ax.plot_surface(alpha, theta, w, cmap='viridis')

# 设置坐标轴标签
ax.set_xlabel('alpha')
ax.set_ylabel('theta')
ax.set_zlabel('w')

# 显示图形
plt.show()
