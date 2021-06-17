#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums, target):
        low = 0
        high = len(nums) - 1
        candidate = []
        if (target not in nums) or (len(nums) == 0):
            return [-1, -1]
        elif len(nums) == 1:
            return [0, 0]
        while low <= high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                candidate.append(mid)
                prev = mid - 1
                after = min(mid + 1, len(nums)-1)
                while (nums[mid] == nums[prev]) and (prev > -1):
                    candidate.append(prev)
                    prev -= 1
                while nums[mid] == nums[after]:
                    candidate.append(after)
                    after += 1
                    if after >= len(nums):
                        break
                low = mid + 1
                high = mid - 1
                return [min(candidate), max(candidate)]
        return [-1, -1]
# @lc code=end

