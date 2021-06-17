#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第 K 大元素
#

# @lc code=start
import heapq
class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.min_heap = []
        for num in nums:
            if len(self.min_heap) < self.k:
                heapq.heappush(self.min_heap, num)
            elif num > self.min_heap[0]:
                heapq.heappushpop(self.min_heap, num)        

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heappushpop(self.min_heap, val)

        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

