"""
每一次变化就会 增加一个段
"""
import collections

n = int(input())
nums = list(map(int, input().split()))

count = 1
for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
        count += 1
print(count)
