#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        flat = []
        for r in matrix:
            flat.extend(r)
        left, right = 0, len(flat) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if flat[mid] == target:
                return True
            elif flat[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
# @lc code=end

