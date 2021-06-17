#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第 K 小的元素
#
# %%
# @lc code=start
import heapq
class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        flat_mat = []
        for r in matrix:
            for c in r:
                flat_mat.append(c)
        heapq.heapify(flat_mat)
        return heapq.nsmallest(k, flat_mat)[-1]
# @lc code=end
# %%
# s = Solution()
# s.kthSmallest([[1, 2], [1, 3]], 2)
# %%
