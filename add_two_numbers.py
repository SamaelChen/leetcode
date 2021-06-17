class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        a = int(''.join([str(x) for x in l1]))
        b = int(''.join([str(x) for x in l2]))
        res = a + b
        res = [int(x) for x in str(res)]
        res.reverse()
        return res


s = Solution()
l1 = [2, 4, 3]
l2 = [5, 6, 4]
s.addTwoNumbers(l1, l2)

l1 = ListNode([2, 4, 3])
l1.val
'a' * 2
