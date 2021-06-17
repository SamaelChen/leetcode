#
# @lc app=leetcode.cn id=685 lang=python3
#
# [685] 冗余连接 II
#
# %%
# @lc code=start
class Solution:
    def findRedundantDirectedConnection(self, edges):
        self.parents = list(range(len(edges) + 1))
        def find(x):
            if self.parents[x] != x:
                self.parents[x] = find(self.parents[x])
            return self.parents[x]
        def union(x, y):
            self.parents[find(x)] = find(y)
        conflict = -1
        cycle = -1
        dummy_parents = list(range(len(edges) + 1))
        for i, e in enumerate(edges):
            if dummy_parents[e[1]] != e[1]:
                conflict = i
            else:
                dummy_parents[e[1]] = e[0]
                if find(e[0]) == find(e[1]):
                    cycle = i
                else:
                    union(e[0], e[1])
        if conflict < 0:
            return [edges[cycle][0], edges[cycle][1]]
        else:
            conflictEdge = edges[conflict]
            if cycle >= 0:
                return [dummy_parents[conflictEdge[1]], conflictEdge[1]]
            else:
                return [conflictEdge[0], conflictEdge[1]]

# class UnionFind:
#     def __init__(self, n):
#         self.ancestor = list(range(n))

#     def union(self, index1: int, index2: int):
#         self.ancestor[self.find(index1)] = self.find(index2)

#     def find(self, index: int) -> int:
#         if self.ancestor[index] != index:
#             self.ancestor[index] = self.find(self.ancestor[index])
#         return self.ancestor[index]


# class Solution:
#     def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
#         nodesCount = len(edges)
#         uf = UnionFind(nodesCount + 1)
#         parent = list(range(nodesCount + 1))
#         conflict = -1
#         cycle = -1
#         for i, (node1, node2) in enumerate(edges):
#             if parent[node2] != node2:
#                 conflict = i
#             else:
#                 parent[node2] = node1
#                 if uf.find(node1) == uf.find(node2):
#                     cycle = i
#                 else:
#                     uf.union(node1, node2)

#         if conflict < 0:
#             return [edges[cycle][0], edges[cycle][1]]
#         else:
#             conflictEdge = edges[conflict]
#             if cycle >= 0:
#                 return [parent[conflictEdge[1]], conflictEdge[1]]
#             else:
#                 return [conflictEdge[0], conflictEdge[1]]

# @lc code=end


# %%
# s = Solution()
# s.findRedundantDirectedConnection([[2, 1], [3, 1], [4, 2], [1, 4]])

# %%
# s.parents
# %%
