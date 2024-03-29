import numpy as np
n,d=map(int,input().split())
q=[]
k=[]
v=[]
for i in range(3):
    for j in range(n):
        t=list(map(int,input().split()))
        match i:
            case 0:
                q.append(t)
            case 1:
                k.append(t)
            case 2:
                v.append(t)
w=np.array(list(map(int,input().split()))).transpose()
k=np.array(k).transpose()
q=np.array(q)
v=np.array(v)
tem=q@k
for i in range(len(tem)):
    for j in range(len(tem[0])):
        tem[i][j]*=w[i]
ans=tem@v
for t in ans:
    print(t)
