import math
n=int(input())
nums=list(map(int,input().split()))
a_v=sum(nums)/n
a_d=0
for num in nums:
    a_d+=(num-a_v)*(num-a_v)
a_d/=n
for num in nums:
    ans=(num-a_v)/math.pow(a_d,0.5)
    print(ans)