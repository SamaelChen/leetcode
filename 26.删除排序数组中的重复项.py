#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# %%
# @lc code=start
class Solution:
    def removeDuplicates(self, nums):
        nums.sort()
        i = 1
        while i < len(nums):
            try:
                if nums[i] == nums[i-1]:
                    del nums[i-1]
                else:
                    i += 1
            except:
                len(nums)
        return len(nums)
# @lc code=end

