#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        board = [None] * n

        def backtrack(n, board, curr=0):
            if curr == n:
                res.append(board[:])
                return 0
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
        return len(res)
# @lc code=end

