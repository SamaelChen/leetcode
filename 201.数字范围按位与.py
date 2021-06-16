#
# @lc app=leetcode.cn id=201 lang=python3
#
# [201] 数字范围按位与
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            shift += 1
            left >>= 1
            right >>= 1
        return left << shift
# @lc code=end

