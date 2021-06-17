#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#
# %%
# @lc code=start
class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = matrix[::-1]
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
# @lc code=end
# %%
