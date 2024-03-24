"""
存储在map 种当key 一样得时候我们可以 计算即可
"""
n,a,b=map(int,input().split())
ab_v={}
ans=0
for i in range(a):
    v=list(map(int, input().split()))
    ab_v[v[0]]=v[1]
for i in range(b):
    v = list(map(int, input().split()))
    if v[0] in ab_v:
        ans+=v[1]*ab_v[v[0]]
print(ans)

