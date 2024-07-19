import numpy as np
x=np.array([[1,2,3,4],[5,2,3,4]])
def constraint(x):
    constraints = [
        x[:,0] + x[:,1] >= 5 , # 线性约束：x0 + x1 >= 5
        
        
    ]
    return np.all(constraints, axis=0)
p=np.zeros((x.shape[0],1))
print(constraint(x))
p[constraint(x)]=500
print(p)
