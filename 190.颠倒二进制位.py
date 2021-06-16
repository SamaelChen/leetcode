#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#
# %%
# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        string = bin(int(n))
        res = int(string[:2] + string[2:].zfill(32)[::-1], 2)
        return res

# @lc code=end
# %%
# s = Solution()
# s.reverseBits(3)