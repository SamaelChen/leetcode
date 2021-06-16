#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0
        m, n, res = len(grid), len(grid[0]), 0
        def find_island(i, j):
            bfs = []
            bfs.append([i, j])
            while len(bfs) > 0:
                i, j = bfs.pop()
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    if i - 1 >= 0:
                        bfs.append([i-1, j])
                    if j - 1 >= 0:
                        bfs.append([i, j-1])
                    if i + 1 < m:
                        bfs.append([i+1, j])
                    if j + 1 < n:
                        bfs.append([i, j+1])
            return
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    find_island(i, j)
                    res += 1
        return res

# @lc code=end

