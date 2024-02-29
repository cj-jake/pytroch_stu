# n = int(input())
# numbers = list(map(int, input().split()))
# numbers.sort()
# # 手动计数
# count_number = {}
# for num in numbers:
#     count_number[num] = count_number.get(num, 0) + 1
#
# # 按照出现次数降序排序
# sorted_number_desc = dict(sorted(count_number.items(), key=lambda x: x[1], reverse=True))
#
# # 打印结果
# for num, count in sorted_number_desc.items():
#     print(f'{num} {count}')
#

#窗口
n,m=map(int,input().split(' '))
windows=[]
for i in range(n):
    window=list(map(int,input().split(' ')))
    windows.append(window)
clicks=[]
for i in range(m):
    click=list(map(int,input().split(' ')))
    clicks.append(click)
tops=[2,1,0]
for click in clicks:
    for top in tops:
        if windows[top][0]<=click[0]<=windows[top][2] and windows[top][1]<=click[1]<=windows[top][3]:
            print(top+1)
            tops.remove(top)
            tops.insert(0,top)
    print("IGNORED")