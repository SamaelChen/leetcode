#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# %%
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        start, end = 0, 0
        res = len(nums) + 1
        csum = 0
        while end < len(nums):
            csum += nums[end]
            while csum >= target:
                csum -= nums[start]
                res = min(res, end - start + 1)
                start += 1
            end += 1
        return res if res != len(nums) + 1 else 0
# @lc code=end
# %%
