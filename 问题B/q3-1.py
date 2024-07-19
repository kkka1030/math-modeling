import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文

def get_width(B,D_0):
    # 初始参数
    alpha = 1.5  # 坡度 (单位: 度)
    D = D_0
    theta = 120  # 换能器的开角 (单位: 度)
    alpha= np.arctan(abs(np.sin(np.radians(B)))*np.tan(np.radians(alpha)))*np.pi+180/np.pi

    #print(D)

    W = D * np.sin(np.radians(theta / 2)) * (
        1 / np.sin(np.radians((180 - theta) / 2 + alpha)) + 1 / np.sin(np.radians((180 - theta) / 2 - alpha)))

    #print(W)
    return W

angle=np.linspace(0,360,360)
W=[]
for i in angle:
    W.append(get_width(i,150))

#print(W)
plt.plot(angle,W)

plt.scatter(90,W[89],color='r')
plt.scatter(270,W[269],color='r')
plt.text(90,W[89],'({}, {})'.format(90,W[89]))
plt.text(270,W[269],'({}, {})'.format(270,W[269]))

angle=np.linspace(0,360,360)
W=[]
for i in angle:
    W.append(get_width(i,149.5))

print(W)
plt.plot(angle,W)

plt.scatter(90,W[89],color='r')
plt.scatter(270,W[269],color='r')
plt.text(90,W[89],'({}, {})'.format(90,W[89]))
plt.text(270,W[269],'({}, {})'.format(270,W[269]))

plt.xlabel("不同角度")
plt.ylabel("覆盖宽度")

plt.show()
