#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# %%
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        while curr is not None:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        h, m = head, slow.next
        slow.next = None
        m = self.reverseList(m)
        while h is not None and m is not None:
            p = m.next
            m.next = h.next
            h.next = m
            h = h.next.next
            m = p
        return
# @lc code=end

# %%
