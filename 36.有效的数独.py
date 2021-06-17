#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board) -> bool:
        for i in range(9):
            exist = []
            for elem in board[i]:
                if elem == '.':
                    continue
                if elem not in exist:
                    exist.append(elem)
                else:
                    return False
            exist = []
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] not in exist:
                    exist.append(board[j][i])
                else:
                    return False
        for l, u in zip([0, 3, 6], [3, 6, 9]):
            for loop in range(3):
                exist = []
                for i in range(l, u):
                    for j in range(3):
                        if board[i][j+3*loop] == '.':
                            continue
                        if board[i][j+3*loop] not in exist:
                            exist.append(board[i][j+3*loop])
                        else:
                            return False
        return True
# @lc code=end

