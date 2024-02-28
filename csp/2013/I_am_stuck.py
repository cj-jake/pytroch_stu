class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y

R,C = map(int,input().split())
maps = []
S_ind = [] # S的坐标
T_ind = [] # T的坐标
for i in range(R):
    temp = list(input())
    if 'S' in temp:
        x = i
        y = temp.index('S')
        S_ind.append(x)
        S_ind.append(y)
    if 'T' in temp:
        x = i
        y = temp.index('T')
        T_ind.append(x)
        T_ind.append(y)
    maps.append(temp)
_type = {
    'S':[[1,0],[-1,0],[0,1],[0,-1]],
    'T':[[1,0],[-1,0],[0,1],[0,-1]],
    '+':[[1,0],[-1,0],[0,1],[0,-1]],
    '-':[[0,1],[0,-1]],
    '|':[[1,0],[-1,0]],
    '.':[[1,0]]
}
# 用来计算上下左右四个点的坐标
round_T = [[1,0],[-1,0],[0,1],[0,-1]]
visited = [[0]*C for i in range(R)] # 初始化

def bounds(x,y):
    if x>=0 and y >= 0 and x<R and y<C:
        return True
    else:
        return False
# 从S点出发遍历
def BFS_S():
    flag = False  # 标记能不能到达目的地
    x = S_ind[0]
    y = S_ind[1]
    queue = []
    queue.append(Node(x,y))
    visited[x][y] = 1
    while queue:
        temp = queue.pop(0)
        x_t = temp.x
        y_t = temp.y
        c = maps[x_t][y_t]
        if c == 'T':
            flag = True
        if c != '#':
            t = _type[c]
            # 这个点周围可以走的点
            for i in t:
                x_i = x_t + i[0]
                y_i = y_t + i[1]
                # 如果这个位置不是不能通行的，并且还没有被访问过
                if bounds(x_i,y_i) and maps[x_i][y_i] != '#' and visited[x_i][y_i] == 0:
                    visited[x_i][y_i] = 1
                    queue.append(Node(x_i,y_i))
    return flag
# 从T点出发遍历
def BFS_T():
    x = T_ind[0]
    y = T_ind[1]
    queue = []
    queue.append(Node(x,y))
    visited[x][y] = 2
    while queue:
        temp = queue.pop(0)
        x_t = temp.x
        y_t = temp.y
        # 查看这个点周围 可以到达这个点的点
        for i in round_T:
            x_i = x_t + i[0]
            y_i = y_t + i[1]
            # 如果这个位置不是不能通行的，并且还没有被访问过
            if bounds(x_i,y_i) and maps[x_i][y_i] != '#' and visited[x_i][y_i] != 2:
                # 如果周围点是+ 或者 S 那么说明它上下左右都可以走，肯定能到达这个点的位置
                if maps[x_i][y_i] == '+' or maps[x_i][y_i] == 'S':
                    visited[x_i][y_i] = 2
                    queue.append(Node(x_i, y_i))
                # 如果周围点是 . 那么这个点必须在 . 的下方,因为 . 只能往下走
                elif maps[x_i][y_i] == '.':
                    if x_i+1 == x_t:
                        visited[x_i][y_i] = 2
                        queue.append(Node(x_i,y_i))
                elif maps[x_i][y_i] == '-' :
                    # 如果周围点是 - 那么在这个点必须在 - 的左方或者右方
                    if ((y_i-1 == y_t) or (y_i+1 == y_t)):
                        visited[x_i][y_i] = 2
                        queue.append(Node(x_i,y_i))
                # 如果周围点是 | 那么这个点必须在 | 的上方或者下方
                elif maps[x_i][y_i] == '|' :
                    if ((x_i-1 == x_t) or (x_i+1 == x_t)):
                        visited[x_i][y_i] = 2
                        queue.append(Node(x_i, y_i))
# 如果可到达目标点
if BFS_S():
    BFS_T()
    sum = 0
    for line in visited:
        sum += line.count(1)
    print(sum)
else:
    print("I'm stuck!")
