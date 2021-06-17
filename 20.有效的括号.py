#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# %%
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        left = ['(', '[', '{']
        right = [')', ']', '}']
        dic = {'(': ')', '[': ']', '{': '}'}
        left_b = []
        if len(s) == 0:
            return True
        if s[0] in right or len(s) % 2 != 0:
            return False
        for x in s:
            if x in left:
                left_b.append(x)
            else:
                if x == dic[left_b[-1]]:
                    left_b.pop()
                else:
                    return False
        if len(left_b) == 0:
            return True
        else:
            return False
# @lc code=end

