#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# %%
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = []
        b = []
        while l1:
            a.append(str(l1.val))
            l1 = l1.next
        while l2:
            b.append(str(l2.val))
            l2 = l2.next
        a.reverse()
        b.reverse()
        a = ''.join(a)
        b = ''.join(b)
        c = str(int(a) + int(b))
        c = [int(x) for x in c]
        c.reverse()
        for idx, item in enumerate(c):
            if idx == 0:
                res = p = ListNode(item)
            else:
                p.next = ListNode(item)
                p = p.next
        return res

    def addTwoNumbersLoop(self, l1, l2):
        prehead = ListNode(0)
        prev = prehead
        a, b = 0, 0
        while l1 and l2:
            tmp = l1.val + l2.val + a
            a, b = tmp // 10, tmp % 10
            prev.next = ListNode(b)
            l1 = l1.next
            l2 = l2.next
            prev = prev.next
        if l1:
            while l1:
                tmp = l1.val + a
                a, b = tmp // 10, tmp % 10
                prev.next = ListNode(b)
                l1 = l1.next
                prev = prev.next
        else:
            while l2:
                tmp = l2.val + a
                a, b = tmp // 10, tmp % 10
                prev.next = ListNode(b)
                l2 = l2.next
                prev = prev.next
        if a != 0:
            prev.next = ListNode(1)
        return prehead.next
# @lc code=end


# %%
# s = Solution()
# l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
# l2 = ListNode(9, ListNode(9))
# res = s.addTwoNumbersLoop(l1, l2)
# while res:
#     print(res.val)
#     res = res.next
# %%
