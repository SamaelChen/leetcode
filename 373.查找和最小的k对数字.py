#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的K对数字
#
# %%
# @lc code=start
import heapq
class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        min_heap = []
        for a in nums1:
            for b in nums2:
                curr_sum = a + b
                heapq.heappush(min_heap, (curr_sum, [a, b]))
        return [x[1] for x in heapq.nsmallest(k, min_heap)]
# @lc code=end
# %%
# s = Solution()
# s.kSmallestPairs([1, 2], [3], 3)
# %%
