#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# %%
# @lc code=start
class Solution:
    def trapBrutal(self, height):
        if len(height) < 3:
            return 0
        res = 0
        left_max = 0
        right_max = 0
        for i in range(1, len(height) - 1):
            for j in range(0, i):
                if height[j] > left_max:
                    left_max = height[j]
            for j in range(i+1, len(height)):
                if height[j] > right_max:
                    right_max = height[j]
            res += max(min(left_max, right_max) - height[i], 0)
            left_max, right_max = 0, 0
        return res
    
    def trap(self, height):
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                curr = height[stack.pop()]
                if not stack:
                    break
                res += (min(height[stack[-1]] - curr, height[i] - curr)) * (i - stack[-1] - 1)
            stack.append(i)
        return res
# @lc code=end
# %%
