n=int(input())
nums=[]
for i in range(n):
    nums.append(list(map(int,input().split())))
visited=[[False]*105 for i in range(105) ]

ans=0
for num in nums:
    x1,y1,x2,y2=num[0],num[1],num[2],num[3]
    while x1<x2:
        t=y1
        while t<y2:
            if visited[x1][t]==False:
                visited[x1][t]=True
                ans+=1
            t+=1
        x1+=1
print(ans)
