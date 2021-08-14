#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#
# %%
# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        target = sum(nums) // k
        # print(target)
        if max(nums) > target:
            return False
        nums.sort(reverse=True)
        visited = set()

        def helper(choose_state, choose_sum):
            # print(bin(choose_state).replace(
            #     '0b', '').zfill(len(nums)), choose_sum)
            if choose_sum == sum(nums):
                return True
            tmp = choose_sum % target
            for i, num in enumerate(nums):
                next_state = choose_state | 1 << i
                if choose_state >> i & 1 == 0 and num + tmp <= target and next_state not in visited:
                    visited.add(next_state)
                    if helper(next_state, choose_sum + num):
                        return True
            return False
        return helper(0, 0)


# @lc code=end
# %%
# s = Solution()
# s.canPartitionKSubsets(nums=[4, 3, 2, 3, 5, 2, 1], k=4)
# s.canPartitionKSubsets(nums=[1, 1, 2], k=2)
# %%
