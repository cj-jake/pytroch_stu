"""
使用一个count记录之前出现的次数 获取最后一个出现值的下标 把该值加一即可

"""
n=int(input())
nums=list(map(int,input().split()))
count=[1]*(len(nums))
for i in range(len(nums)):
    if nums[i] in nums[:i]:
        # 从0到i-1的列表
        sublist = nums[:i]
        # 获取sublist中最后一个元素
        last_index = len(sublist) - sublist[::-1].index(nums[i]) - 1
        count[i]=count[last_index]+1
for i in range(len(nums)):
    print(count[i],end=' ')
