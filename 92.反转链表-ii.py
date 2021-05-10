#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# %%
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head is None or left == right:
            return head
        if left > right:
            return None
        dummy = ListNode(None, next=None)
        idx = 1
        curr, peek = None, head
        if left == 1:
            left_lst = dummy
        while peek is not None:
            if idx < left:
                if idx == 1:
                    left_lst = ListNode(peek.val, next=None)
                    dummy.next = left_lst
                else:
                    left_lst.next = peek
                    left_lst = left_lst.next
            elif idx >= left and idx <= right:
                if idx == left:
                    tail = ListNode(peek.val, next=None)
                    pre = tail
                else:
                    pre = ListNode(peek.val, next=curr)
                curr = pre
                if idx == right:
                    left_lst.next = pre
                    left_lst = tail
            else:
                left_lst.next = peek
                left_lst = left_lst.next
            peek = peek.next
            idx += 1
        return dummy.next
# @lc code=end

# %%
