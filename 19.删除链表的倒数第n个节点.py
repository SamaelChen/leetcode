#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dum = ListNode(0)
        dum.next = head
        f = head
        s = dum
        for _ in range(n-1):
            f = f.next
        while f and f.next:
            f = f.next
            s = s.next
        s.next = s.next.next
        return dum.next
# @lc code=end

