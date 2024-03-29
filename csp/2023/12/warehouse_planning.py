"""
记录每一个坐标的最小值和最大值 选仓库的上级的时候只需要选择大于此最大值的的最小就可以
"""
n,m=map(int,input().split())
sites=[]
for i in range(n):
    sites.append(list(map(int, input().split())))

for i in range(n):
    output=0
    for j in range(n):
        if i!=j:
            falg = True
            for k in  range(m):
                if sites[i][k]>=sites[j][k]:
                    falg=False
                    break
            if falg:
                output=j+1
                break
    print(output)

"""
n, m = map(int, input().split())
warehouse = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    output = 0
    for j in range(n):
        if i!=j:
            flag = True
            for k in range(m):
                if warehouse[i][k]>=warehouse[j][k]:
                    flag = False
                    break
            if flag:
                output = j+1
                break
    print(output)
"""