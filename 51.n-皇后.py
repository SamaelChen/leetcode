#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
# %%
# @lc code=start
class Solution:
    def solveNQueens(self, n):
        res = []
        final = []
        board = [None] * n
        def backtrack(n, board, curr=0):
            if curr == n:
                res.append(board[:])
                return
            for i in range(n):
                board[curr] = i
                flag = True
                for j in range(curr):
                    if board[j] == i or abs(i - board[j]) == curr - j:
                        flag = False
                        break
                if flag:
                    backtrack(n, board, curr+1)
        backtrack(n, board, curr=0)
        for board_res in res:
            b = []
            for _ in range(n):
                b.append('.' * n)
            for r, c in enumerate(board_res):
                b[r] = b[r][:c] + 'Q' + b[r][(c+1):]
            final.append(b)
        return final
# @lc code=end
# %%