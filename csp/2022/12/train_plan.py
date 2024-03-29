import collections

n, m = map(int, input().split())
start = list(map(int, input().split()))
numbers = list(map(int, input().split()))

# 计算最早开始时间
num_start = [1] * m
for i in range(1, m):
    if start[i] != 0:  # 表明存在依赖关系
        num_start[i] = numbers[start[i] - 1] + num_start[start[i] - 1]
flag = False
for i in range(m):
    # 计算最早完成时间
    finsh_t = num_start[i] + numbers[i]
    if num_start[i] + numbers[i] > n + 1 and not flag:
        flag = True
        print(*num_start)
    # 上面代码可以拿到70分
if not flag:
    # 计算最晚开始时间
    """
    没有被依赖
    n-所需要时间就是最晚开始时间 
    如果被依赖 需要考虑后面依赖最后完成时间
    
    """
    # 记录被引用

    back_citation = collections.defaultdict(lambda: [])
    for i, s in enumerate(start):
        if s != 0:
            back_citation[s].append(i + 1)
    ans = [0] * m
    for i in range(m):
        tem = 0
        if (i + 1) in back_citation.keys():
            values = back_citation[i + 1]
            for v in values:
                tem = max(tem, numbers[v - 1])
        ans[i] = n - numbers[i] - tem+1
    print(*num_start)
    print(*ans)
