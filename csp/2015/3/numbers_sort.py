n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
# 手动计数
count_number = {}
for num in numbers:
    count_number[num] = count_number.get(num, 0) + 1

# 按照出现次数降序排序
sorted_number_desc = dict(sorted(count_number.items(), key=lambda x: x[1], reverse=True))

# 打印结果
for num, count in sorted_number_desc.items():
    print(f'{num} {count}')