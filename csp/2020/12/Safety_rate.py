n=int(input())
nums=[]
for i in range(n):
    nums.append(list(map(int,input().split())))
ans=0
for x,y in nums:
    ans+=x*y
ans=max(0,ans)
print(ans)