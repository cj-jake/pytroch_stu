"""
逆序 按照列输出就行

"""
# 读取数据
n,m=map(int,input().split())
maritx=list()
for i in range(n):
    maritx.append(list(map(int,input().split())))

for i in range(m):
    for j in range(n):
        print(maritx[j][-1 - i],end=" ")
    print()


