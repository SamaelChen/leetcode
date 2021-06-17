#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# %%
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int):
        if n == 0:
            return []
        parenthesisList = []
        parenthesisList.append([None])
        parenthesisList.append(["()"])
        for i in range(2, n+1):
            l = []
            for j in range(i):
                list1 = parenthesisList[j]
                list2 = parenthesisList[i-1-j]
                for k1 in list1:
                    for k2 in list2:
                        if k1 is None:
                            k1 = ''
                        if k2 is None:
                            k2 = ''
                        el = '(' + k1 + ')' + k2 #新增的一个括号要么包住原有的序列，要么在外面，在外面的时候在左边和右边是一样的
                        l.append(el)
            parenthesisList.append(l)
        return parenthesisList[n]
# @lc code=end
