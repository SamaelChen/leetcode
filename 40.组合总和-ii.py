#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# %%
# @lc code=start
class Solution:
    def combinationSum2(self, candidates, target):
        # 将数组进行升序排序
        candidates.sort()

        # 结果列表
        ans = []
        # 可能组合
        tmp = []

        def helper(idx, total):
            if total == target:
                ans.append(tmp[::])
                return
            if total > target:
                return

            for i in range(idx, len(candidates)):
                # 这里限制同一层不能选择值相同的元素
                # 若有相同的元素，优先选择索引靠前的
                if candidates[i-1] == candidates[i] and i-1 >= idx:
                    continue

                total += candidates[i]
                tmp.append(candidates[i])
                # 这里注意，与 39 题不同，进入递归下一层
                # 从当前索引的下一位开始选取，避免重复选取同个元素
                helper(i+1, total)
                # 回溯
                tmp.pop()
                total -= candidates[i]

        total = 0
        helper(0, total)
        return ans
# @lc code=end