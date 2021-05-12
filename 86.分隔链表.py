#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small, large = ListNode(), ListNode()
        a, b = small, large
        while head is not None:
            if head.val < x:
                a.next = ListNode(head.val)
                a = a.next
            else:
                b.next = ListNode(head.val)
                b = b.next
            head = head.next
        a.next = large.next
        return small.next
# @lc code=end

