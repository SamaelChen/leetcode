#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#
# %%
# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 1:
            return '1'
        pre = self.countAndSay(n-1)
        res = ''
        for i in range(len(pre)):
            if i == 0:
                cnt = 1
            elif pre[i] == pre[i-1]:
                cnt += 1
            else:
                tmp = str(cnt)+pre[i-1]
                res += tmp
                cnt = 1
            if i == len(pre) - 1:
                tmp = str(cnt)+pre[i]
                res += tmp
        return res

# @lc code=end
