#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            res = nums.index(target)
        except:
            res = -1
        return res
# @lc code=end

