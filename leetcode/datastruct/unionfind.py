import collections
from typing import List


class UnionFind:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


def findCircleNum(self, isConnected: List[List[int]]) -> int:
    def find(self, x: int) -> int:
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(self, x: int, y: int):
        parent[find(x)] = find(y)

    cities = len(isConnected)
    parent = list(range(cities))
    for i in range(cities):
        for j in range(i + 1, cities):
            if isConnected[i][j] == 1:
                union(i, j)
    ans = sum(parent[i] == i for i in range(cities))
    return ans

    # 使用站实现


def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    stk = collections.deque(0)
    path = [0]
    ans = []
    while stk:
        node = stk.pop()
        if node == len(graph) - 1:
            ans.append(path[:])
        # 查看node 和那些边相连接
        for y in graph[node]:
            path.append(y)
            stk.append(y)
            path.pop()
    return ans
