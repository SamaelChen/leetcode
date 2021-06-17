#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
# %%
# @lc code=start


class Solution:
    def check(self, board, row, col, num):
        board_T = [[board[i][j] for i in range(9)] for j in range(9)]
        if num in board[row]:
            return False
        if num in board_T[col]:
            return False
        x = row // 3 * 3
        y = col // 3 * 3
        for i in range(x, x+3):
            for j in range(y, y+3):
                if num == board[i][j]:
                    return False
        return True

    def move(self, board, idx=0):
        num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        if idx == 81:
            return True
        i, j = idx // 9, idx % 9
        if board[i][j] == '.':
            for n in num:
                if self.check(board, i, j, n):
                    board[i][j] = n
                    if not self.move(board, idx+1):
                        board[i][j] = '.'
                    else:
                        return True
            return False
        else:
            if not self.move(board, idx+1):
                return False


    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.move(board, 0)

# @lc code=end


# %%
s = Solution()
a = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."],
     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
s.solveSudoku(a)

# %%
