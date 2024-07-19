import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei'] # 显示中文

def sin(a):
    return np.sin(np.radians(a))

def cos(a):
    return np.cos(np.radians(a))

def tan(a):
    return np.tan(np.radians(a))

angle = np.linspace(0, 360, 360)
low = 110 - 2 * 1852 * np.tan(np.radians(1.5))
high = 110 + 2 * 1852 * np.tan(np.radians(1.5))

alpha = 1.5 # 坡度 (单位，度)
theta = 120 # 开角 (单位，度)

n = np.linspace(0.1, 0.2, 100)
cnt = []

for i in n:
    x = sin(theta / 2) * cos(alpha) * high / (sin(90 - theta / 2 - alpha) + sin(alpha) * sin(theta / 2))
    x = high - x * tan(alpha)
    #print(x)
    ans = []
    ans.append(x)
    A = sin(90 - theta / 2 + alpha)
    B = sin(90 - theta / 2 - alpha)
    C = sin(theta / 2) / A - 1 / tan(alpha)
    D = i * sin(theta / 2) * (1 / A + 1 / B) - sin(theta / 2) / B - 1 / tan(alpha)

    while True:
        x = x * C / D
        if x < low:
            break
        ans.append(x)

    cnt.append(len(ans))

n = np.array(n)
#print(n)
print(cnt)
plt.plot(n, cnt, color='r')
plt.xlabel("不同重复率")
plt.ylabel("测线总数")
plt.show()
