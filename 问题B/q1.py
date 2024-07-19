import pandas as pd
import numpy as np

# 初始化参数
D_0 = 70
theta = 120
alpha = 1.5
d = 200

D = d * np.sin(np.radians(90 - theta / 2)) / np.sin(np.radians(90 - alpha + theta / 2))

distances = np.array([-800, -600, -400, -200, 0, 200, 400, 600, 800])
D=D_0 - distances * np.tan(np.radians(alpha))

print(D)

W = D * np.sin(np.radians(theta / 2)) * (1 / np.sin(np.radians((180 - theta) / 2 + alpha)) + 1 / np.sin(np.radians((180 - theta) / 2 - alpha)))

print(W)

n = 1 - d / W

print(n)

# 创建 DataFrame 用于保存结果
df = pd.DataFrame({
    '模拟距离中心点处的距离/m': distances,
    '海水深度/m': D,
    '震差宽度/m': W,
    '与前一条测线的重叠率/%': n
})

# 将 DataFrame 保存为 Excel 文件
path = r'C:\Users\31019\Desktop\mathematical modeling\问题B\res1.xlsx'
df.to_excel(path, index=False)

