#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# %%
# @lc code=start
class Solution:
    def generateMatrix(self, n):
        mat = [[None]*n for _ in range(n)]
        path = []
        r, c = 0, 0
        upper_margin_r = 0
        left_margin_c = 0
        bottom_margin_r = n - 1
        right_margin_c = n - 1
        i = 1
        while i <= (n*n):
            mat[r][c] = i
            i += 1
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
        return mat
# @lc code=end
# %%
