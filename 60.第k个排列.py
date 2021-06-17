#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#
# %%
# @lc code=start
class Solution:
    def getPermutation(self, n, k):
        factorial = [1]
        for i in range(1, n+1):
            factorial.append(factorial[-1] * i)
        if k > factorial[-1]:
            return ''
        elements = []
        for i in range(n):
            elements.append(i + 1)
        ans = []
        idx = len(factorial) - 1
        while len(ans) < n:
            order = k // factorial[idx-1]
            residual = k % factorial[idx-1]
            if residual == 0 and order != 0:
                order -= 1
            k -= factorial[idx-1] * order
            ans.append(str(elements[order]))
            elements.remove(elements[order])
            idx -= 1
        return ''.join(ans)
            
# @lc code=end

# %%
