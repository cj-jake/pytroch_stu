"""

问题描述
　　目前在一个很大的平面房间里有 n 个无线路由器,每个无线路由器都固定在某个点上。任何两个无线路由器只要距离不超过 r 就能互相建立网络连接。
　　除此以外,另有 m 个可以摆放无线路由器的位置。你可以在这些位置中选择至多 k 个增设新的路由器。
　　你的目标是使得第 1 个路由器和第 2 个路由器之间的网络连接经过尽量少的中转路由器。请问在最优方案下中转路由器的最少个数是多少?
输入格式
　　第一行包含四个正整数 n,m,k,r。(2 ≤ n ≤ 100,1 ≤ k ≤ m ≤ 100, 1 ≤ r ≤ 108)。
　　接下来 n 行,每行包含两个整数 xi 和 yi,表示一个已经放置好的无线 路由器在 (xi, yi) 点处。输入数据保证第 1 和第 2 个路由器在
    仅有这 n 个路由器的情况下已经可以互相连接(经过一系列的中转路由器)。
　　接下来 m 行,每行包含两个整数 xi 和 yi,表示 (xi, yi) 点处可以增设 一个路由器。
　　输入中所有的坐标的绝对值不超过 108,保证输入中的坐标各不相同。
输出格式
　　输出只有一个数,即在指定的位置中增设 k 个路由器后,从第 1 个路 由器到第 2 个路由器最少经过的中转路由器的个数。
样例输入
5 3 1 3
0 0
5 5
0 3
0 5
3 5
3 3
4 4
3 0
样例输出
2
"""
from collections import deque


class Node:
    def __init__(self, x=0, y=0, step=0, k=0):
        self.x = x
        self.y = y
        self.step = step
        self.k = k

maxn = 205  # 假设maxn为某个值
visit=[False]*maxn
map_array = [Node() for _ in range(maxn)]

def bfs(begin:int,end:int):
    q=deque()
    q.appendleft(Node(map_array[begin].x,map_array[begin].y,0,0))
    visit[begin]=True#访问过的节点 标记

    #遍历
    while q:
        s=q.pop()
        #到达了 对应的位置
        if s.x == map_array[end].x and s.y == map_array[end].y:
            return s.step - 1  # 求出中转个数
        if s.k==k:
            max1=n
        else:
            max1=n+m
        for i in  range(1,max1+1):
            #跳过遍历过的
            if visit[i]:
                continue
            #查看距离 是否小于r
            distance_squared = (map_array[i].x - s.x) ** 2 + (map_array[i].y - s.y) ** 2
            if distance_squared>r**2:
                continue
            visit[i]=True
            kk=s.k+1 if i>n else s.k
            q.appendleft(Node(map_array[i].x, map_array[i].y, s.step + 1, kk))  # 走进去，放进队列中



n,m,k,r=map(int,input().split(' '))
for i in range(n+m):
    map_array[i].x,map_array[i].y=map(int,input().split(' '))
print(bfs(0,1))







