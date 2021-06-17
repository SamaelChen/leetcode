#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        res = 0
        for i in range(len(s)):
            if not stack or s[i] == '(' or s[stack[-1]] == ')':
                stack.append(i)
            else:
                stack.pop()
                res = max(res, i - (stack[-1] if stack else -1))
        return res
# @lc code=end

