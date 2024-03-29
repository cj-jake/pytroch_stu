n,N=map(int,input().split())
numbers=list(map(int,input().split()))
r=N//(n+1)
j=0
ans=0
for i in range(1,N):
    if i in numbers:
        j+=1
    g=i//r
    ans+=abs(g-j)
print(ans)
