from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# 加载数据集
data = load_iris()
X, y = data.data, data.target

# 初始化模型
model = RandomForestClassifier()

# 进行5折交叉验证
scores = cross_val_score(model, X, y, cv=5)

# 输出交叉验证结果
print("Cross-validation scores:", scores)
print("Mean cross-validation score:", scores.mean())

