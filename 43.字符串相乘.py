#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start

class Solution(object):
    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'
        res = [0]*(len(num1)+len(num2))
        for index1, i in enumerate(num1[::-1]):
            for index2, j in enumerate(num2[::-1]):
                tmp = res[index1+index2] + int(i)*int(j)
                res[index1+index2] = tmp % 10
                res[index1+index2+1] += tmp//10
        result = ''
        for i in res[::-1]:
            result += str(i)

        return result.lstrip('0')
# @lc code=end

