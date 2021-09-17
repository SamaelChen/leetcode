#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# %%
# @lc code=start
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()

# @lc code=end

# %%
# s = Solution()
# s.merge([1,2,3,0,0,0],3,[2,5,6],3)
# %%
