#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        curr, peek = None, head
        while peek is not None:
            pre = ListNode(peek.val, next=curr)
            curr = pre
            peek = peek.next
        return pre
# @lc code=end
