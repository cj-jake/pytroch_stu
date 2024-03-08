"""
横向和纵向之后 往右和往下 两个方向并且只是移动一次 之后分别对应 往左下和右上
左下和右上改变方向实在遇到边界时
整个遍历方向就是往右 左下 向下 右上 在循环
定义一个方向 表示往右 左下 向下 右上

复杂度有点高 但是过了

"""
dirction = [[0, 1],[1, -1], [1, 0], [-1, 1]]

# 读入数据
n = int(input())
matrix = [[] for _ in range(n)]
for i in range(n):
    matrix[i]=list(map(int, input().split()))
falg=0
i = 0
j = 0
while i<n and j<n:
    #只需第一时打印
    if falg==0:
        print(matrix[i][j],end=' ')
        falg+=1
    for x in range(4):
        if x==1 or x==3:
            i = i + dirction[x][0]
            j = j + dirction[x][1]
            while 0<=i<n and 0<=j<n:
                if 0 <= i < n and 0 <= j < n:
                    print(matrix[i][j],end=' ')
                    i = i + dirction[x][0]
                    j = j + dirction[x][1]
            i = i- dirction[x][0]
            j = j - dirction[x][1]
        else:
            i = i + dirction[x][0]
            j = j + dirction[x][1]
            if 0 <= i < n and 0 <= j < n:
                print(matrix[i][j],end=' ')




