#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
# %%
# @lc code=start
class Solution:
    def largestRectangleAreaBrutal(self, heights) -> int:
        res = float('-inf')
        for left in range(len(heights)):
            min_height = heights[left]
            num = 1
            max_area = min_height * num
            for right in range(left+1, len(heights)):
                min_height = min(heights[right], min_height)
                num += 1
                max_area = max(min_height * num, max_area)
            res = max(res, max_area)
        return res

    def largestRectangleArea(self, heights):
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while len(stack) > 1 and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                max_area = max(max_area, h * (i - stack[-1] - 1))
            stack.append(i)
        while len(stack) > 1:
            h = heights[stack.pop()]
            max_area = max(max_area, h*(len(heights) - stack[-1] - 1))
        return max_area


# @lc code=end


# %%
# s = Solution()
# s.largestRectangleArea([2, 1, 5, 6, 2, 3])

# %%
