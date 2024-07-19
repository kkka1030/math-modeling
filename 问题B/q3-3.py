import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文

def sin(a):
    return np.sin(np.radians(a))

def cos(a):
    return np.cos(np.radians(a))

def tan(a):
    return np.tan(np.radians(a))

def get_Wleft(D):
    return D*sin(theta/2)/sin(90-theta/2-alpha)



angle=np.linspace(0,360,360)
low=110-2*1852*np.tan(np.radians(1.5))
high=110+2*1852*np.tan(np.radians(1.5))

alpha=1.5 #坡度（单位：度）
theta=120 #挖掘铲的开角（单位：度）

n=0.1
cnt=[]
x=sin(theta/2)*cos(alpha)*high/(sin(90-theta/2-alpha)+sin(alpha)*sin(theta/2))
x=high-x*tan(alpha)

print(x)
ans=[]
ans.append(x)

A = sin(90 - theta / 2 + alpha)
B = sin(90 - theta / 2 - alpha)
C = sin(theta / 2) / A - 1 / tan(alpha)
D = n * sin(theta / 2) * (1 / A + 1 / B) - sin(theta / 2) / B - 1 / tan(alpha)

while True:
    x = x * C / D
    if x < low:
        break
    ans.append(x)


index=np.arange(len(ans))
ans=np.array(ans)
dis=[]

for i in range(len(ans)-1):
    dis.append((ans[i]-ans[i+1])/tan(alpha))

for i in range(len(dis)-1):
    dis[i+1]+=dis[i]
    
#print(dis)
#plt.scatter(index,ans,color='g')
#plt.xlabel("测线编号")
#plt.ylabel("水深")
#plt.show()
print(dis)
dis.insert(0,0)
dis=np.array(dis)/1852
y=np.zeros(len(dis))

#plt.scatter(dis,y,marker='x',s=10)
plt.xlabel("各测线的水平位置")
plt.ylim(-1.2,1.2)
plt.yticks(alpha=0)
plt.tick_params(axis='y',width=0)
y=np.linspace(-1,1,10000)

for i in range(len(dis)-1):
    x=np.full((1,10000),dis[i])
    plt.scatter(x,y,s=0.0001,color='c')
    tx=np.linspace(dis[i],dis[i+1],1000)
    if i%2==0:
        ty=1
    else:
        ty=-1
    ty=np.full((1,1000),ty)
    plt.scatter(tx,ty,s=0.0001,color='c')
x=np.full((1,10000),dis[-1])
plt.scatter(x,y,s=0.0001,color='c')
plt.show()
path=r'C:\\Users\\31019\\Desktop\\mathematical modeling\\问题B\\距高.xlsx'
# pd.DataFrame(dis).to_excel(path)
# path=r'C:\Users\PC\Desktop\水深.xlsx'
# pd.DataFrame(ans).to_excel(path)
