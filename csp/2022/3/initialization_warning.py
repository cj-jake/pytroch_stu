import collections

n,k=map(int,input().split())
right_value=collections.defaultdict(lambda :0)
ans=0
for i in range(k):
    right,value=map(int,input().split())
    if value!=0 and value not in right_value.keys():
        ans+=1
    right_value[right]+=1
print(ans)