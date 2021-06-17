#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# %%
# @lc code=start
class Solution:
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        r = 0
        c = 0
        res = []
        path = []
        upper_margin_r = 0
        left_margin_c = 0
        bottom_margin_r = rows - 1
        right_margin_c = cols - 1
        while len(res) < (rows*cols):
            res.append(matrix[r][c])
            path.append([r, c])
            if c < right_margin_c and r == upper_margin_r:
                c += 1
            elif c == right_margin_c and r < bottom_margin_r:
                r += 1
            elif r == bottom_margin_r and c > left_margin_c:
                c -= 1
            elif c == left_margin_c and r > upper_margin_r:
                r -= 1
            if [r, c] in path:
                r += 1
                c += 1
                bottom_margin_r -= 1
                right_margin_c -= 1
                upper_margin_r += 1
                left_margin_c += 1
        return res
# @lc code=end
# %%
