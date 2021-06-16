#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import collections

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return node
        visited = {node: Node(node.val, [])}
        bfs = collections.deque([node])
        while len(bfs) > 0:
            curr = bfs.popleft()
            curr_copy = visited[curr]
            for n in curr.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val, [])
                    bfs.append(n)
                curr_copy.neighbors.append(visited[n])
        return visited[node]
# @lc code=end

