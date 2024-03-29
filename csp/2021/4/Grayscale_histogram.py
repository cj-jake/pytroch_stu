import collections

n,m,l=map(int,input().split())
ans={i:0 for i in range(0,l)}
grap=[]
for i in range(n):
    grap.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        ans[grap[i][j]]+=1

for k,v in ans.items():
    print(v,end=' ')
