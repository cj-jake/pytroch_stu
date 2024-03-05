"""
按照题目所说模拟
"""
#读入数据
def dfs(x:int,y:int,c:str):
    if not (0 <= x <= n - 1 and 0 <= y <= m - 1):
        return
    if (canvas[x][y] != '-' and canvas[x][y] != '|' and canvas[x][y] != '+'):
        canvas[x][y] = c
        # 分别填充上下左右四个位置
    for i in range(len(direction)):
        # 不要忘记更新坐标  坐标从左下角开始
        newx, newy = map(int, [direction[i][0] + x, direction[i][1] + y])
        dfs(newx,newy,c)
        # while (0 <= newx <= n - 1 and 0 <= newy <= m - 1):
        #     if canvas[newx][newy] == '_' or canvas[newx][newy] == '|':
        #         break
        #     canvas[newx][newy] = c
        #     newx, newy = map(int, [direction[i][0] + newx, direction[i][1] + newy])
m,n,q=map(int,input().split())
canvas=[['.']*m for _ in range(n)]
commands=[]
#用来记录上下左右四个放行
direction=[[0,1],[0,-1],[-1,0],[1,0]]
for i in range(q):
    commands.append(list(input().split()))

for command in commands:
    #命令长度为是4表示 填充
    if len(command)==4:
        x,y,c=n-int(command[1])-1,int(command[2]),command[3]

    else:
        x1,y1,x2,y2=n-int(command[2])-1,int(command[1]),n-int(command[4])-1,int(command[3])
        if x1==x2:
            #使用横线填充 如果已经有竖线填充过则变为+ 下面同理
            for y in range(y1,y2+1):
                if not 0<=y<m:
                    break
                if canvas[x1][y]=='|':
                    canvas[x1][y]='+'
                else:
                    canvas[x1][y] = '-'
        elif y1==y2:
            #使用竖线填充
            for x in range(x1,x2+1):
                if not 0<=x<n:
                    break
                if canvas[x][y1]=='-':
                    canvas[x][y1]='+'
                else:
                    canvas[x][y1] = '|'

#输出画布
for i in range(n):
    for j in range(m):
        print(f'{canvas[i][j]} ',end='')
    print()