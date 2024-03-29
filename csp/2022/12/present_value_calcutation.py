t = list(input().split())
n = int(t[0])
r = float(t[1])
nums = list(map(int, input().split()))
ans = nums[0]
for i in range(1,len(nums)):
   ans += nums[i]*pow(1+r,-i)
print(ans)
