class Solution:
    def twoSum(self, nums, target):
        for i in range(0, len(nums) - 1):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


s = Solution()
s.twoSum([1, 2, 3, 4, 5, 6], 4)


class Solution2:
    def twoSum(self, nums, target):
        for index, x in enumerate(nums):
            diff = target - x
            if diff in nums[(index + 1):]:
                return [index, nums.index(diff)]


s = Solution2()
s.twoSum([3, 3], 6)


class Solution3(object):
    def twoSum(self, nums, target):
        mapping = {}

        for index, val in enumerate(nums):
            diff = target - val
            if diff in mapping:
                return [index, mapping[diff]]
            else:
                mapping[val] = index


s = Solution3()
s.twoSum([3, 3], 6)


class Solution4:
    def twoSum(self, nums, target):
        for idx, n in enumerate(nums):
            residual = target - n
            if residual in nums[(idx + 1):]:
                return(idx, nums[(idx + 1):].index(residual) + idx + 1)


s = Solution4()
s.twoSum([3, 3], 6)
s.twoSum([1, 2, 3, 4, 5, 6], 4)
