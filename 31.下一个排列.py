#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# %%
# @lc code=start
class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2: return
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                for j in range(len(nums)-1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                nums[(i+1):] = sorted(nums[(i+1):])
                return
        return nums.sort()
# @lc code=end

