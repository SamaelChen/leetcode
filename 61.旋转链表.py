#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
# %%
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head, k):
        if head is None or head.next is None or k <= 0:
            return head
        length, cur = 1, head
        while cur.next is not None:
            length += 1
            cur = cur.next
        cur.next = head
        for _ in range(length - k % length):
            cur = cur.next
        head, cur.next = cur.next, None
        return head
# @lc code=end
