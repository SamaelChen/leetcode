#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#
# %%
# @lc code=start
class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            if sum([math.ceil(p / mid) for p in piles]) > h:
                left = mid + 1
            else:
                right = mid - 1
        return left
# @lc code=end

