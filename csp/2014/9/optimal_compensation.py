from collections import deque


class Node:
    def __init__(self, x, y, dis):
        self.x = x
        self.y = y
        self.dis = dis


n, m, k, d = map(int, input().split())
v = [(-1, 0), (1, 0), (0, -1), (0, 1)]
vis = [[0] * (n + 1) for _ in range(n + 1)]
order = [[0] * (n + 1) for _ in range(n + 1)]
Q = deque()


def init():
    for _ in range(m):
        a, b = map(int, input().split())
        Q.append(Node(a, b, 0))

    for _ in range(k):
        a, b, c = map(int, input().split())
        order[a][b] += c

    for _ in range(d):
        a, b = map(int, input().split())
        vis[a][b] = 1


def solve():
    ans = 0
    while Q:
        t = Q.popleft()
        x, y, dis = t.x, t.y, t.dis
        for dx, dy in v:
            xx, yy = x + dx, y + dy
            if 1 <= xx <= n and 1 <= yy <= n and not vis[xx][yy]:
                ans += order[xx][yy] * (dis + 1)
                vis[xx][yy] = 1
                Q.append(Node(xx, yy, dis + 1))
    print(ans)


if __name__ == "__main__":
    init()
    solve()
