"""
我们每一个点 上下 或者 左右 相同需要同时被删除
接着往下走 我们开辟一个n*m 的空间去标记哪一个需要被删除

"""
#输入数据
n,m=map(int,input().split())
matrix=[[0]*m for _ in range(n)]
for i in range(n):
    matrix[i]=list(map(int,input().split()))

direction=[[0,1],[0,-1],[-1,0],[1,0]]
#等于1表示需要删除
matrix_del=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        #左右相同 活着上下相同把他标记为需要删除
        newx1,newy1=i+direction[0][0],j+direction[0][1]
        newx2,newy2=i+direction[1][0],j+direction[1][1]
        #边界检查
        if 0<=newx1<=n-1 and 0<=newy1<=m-1 and 0<=newx2<=n-1 and 0<=newy2<=m-1:
            if (matrix[i][j]==matrix[newx1][newy1])and(matrix[i][j]==matrix[newx2][newy2]):
                #标记要删除的点
                matrix_del[i][j]=matrix_del[newx1][newy1]=matrix_del[newx2][newy2]=1
        #上下 和上面类似
        newx3,newy3=i+direction[2][0],j+direction[2][1]
        newx4,newy4=i+direction[3][0],j+direction[3][1]
        if 0<=newx3<=n-1 and 0<=newy3<=m-1 and 0<=newx4<=n-1 and 0<=newy4<=m-1:
            if (matrix[i][j]==matrix[newx3][newy3]) and matrix[i][j]==matrix[newx4][newy4]:
                #标记要删除的点
                matrix_del[i][j]=matrix_del[newx3][newy3]=matrix_del[newx4][newy4]=1



#遍历输出
for i in range(n):
    for j in range(m):
        if matrix_del[i][j]==1:
            print('0 ',end='')
        else:
            print(f'{matrix[i][j]} ',end='')
    print()
