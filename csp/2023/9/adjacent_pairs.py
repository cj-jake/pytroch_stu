n = int(input())  # 输入一个整数 n，表示列表的长度
nums = list(map(int, input().split(' ')))  # 输入一个空格分隔的整数列表
nums.sort()  # 对整数列表进行升序排序
ans = 0  # 初始化计数器 ans 为 0

# 遍历整数列表，统计相邻数字连续的对数
for i in range(1, n):
    if nums[i] ==(nums[i - 1] + 1):
        ans += 1

# 输出最终的连续对数
print(ans)
