#
# @lc app=leetcode.cn id=1584 lang=python3
#
# [1584] 连接所有点的最小费用
#
# %%
# @lc code=start


class UnionFind:
    def __init__(self, n) -> None:
        self.parents = list(range(n))
        self.size = [1] * n
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, x, y):
        xroot, yroot = self.find(x), self.find(y)
        if xroot == yroot:
            return False
        else:
            if self.size[xroot] < self.size[yroot]:
                self.parents[xroot] = yroot
                self.size[yroot] += self.size[xroot]
            else:
                self.parents[yroot] = xroot
                self.size[xroot] += self.size[yroot]
        return True

class Solution:
    def minCostConnectPointsKruskal(self, points) -> int:
        # kruskal
        if len(points) == 1:
            return 0

        def dist(x, y): return abs(
            points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])
        edges = []
        res, n = 0, 1
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                edges.append((dist(i, j), i, j))
        edges.sort()
        uf = UnionFind(len(points))
        for length, x, y in edges:
            if uf.union(x, y):
                res += length
                n += 1
                if n == len(points):
                    break
        return res

    def minCostConnectPointsPrimOwn(self, points):
        dist = lambda x, y: abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])
        n = len(points)
        visted = [0] * n
        visted[0] = 1
        res = 0
        while sum(visted) < n:
            minimum = float('inf')
            for i in range(n):
                if visted[i] == 1:
                    for j in range(n):
                        if visted[j] == 0:
                            if minimum > dist(i, j):
                                minimum = dist(i, j)
                                select = j
            visted[select] = 1
            print(minimum, visted)
            res += minimum
        return res

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # 构建邻接表
        graph = defaultdict(lambda: defaultdict())
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                d = abs(x2-x1)+abs(y2-y1)
                graph[i][j] = d
                graph[j][i] = d

        res = 0
        visited = set()
        dist = [float('inf')]*n
        dist[0] = 0
        # 构建最小生成树
        for i in range(n):
            min_ = float('inf')
            node = -1
            for j in range(n):
                if j not in visited and dist[j] < min_:
                    node = j
                    min_ = dist[j]
            visited.add(node)
            res += dist[node]
            for nex in graph[node]:
                if nex not in visited and graph[node][nex] < dist[nex]:
                    dist[nex] = graph[node][nex]
        return res

# @lc code=end
# %%
# s = Solution()
# s.minCostConnectPointsPrim([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]])
# s.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]])

# %%
