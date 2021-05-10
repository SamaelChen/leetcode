#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.remain = None
    def reverseBetween(self, head, right):
        if head.next == right:
            self.remain = head.next
            return head
        last = self.reverseBetween(head.next, right)
        head.next.next = head
        head.next = self.remain
        return last
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        a = b = head
        for _ in range(k):
            if b is None:
                return head
            b = b.next
        last = self.reverseBetween(a, b)
        a.next = self.reverseKGroup(b, k)
        return last
# @lc code=end

