#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# %%
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        dummy = ListNode(next=head)
        curr, peek = dummy, head
        duplicated = False
        while peek.next is not None:
            if peek.val == peek.next.val:
                duplicated = True
                peek.next = peek.next.next
            else:
                if duplicated:
                    duplicated = False
                    curr.next = curr.next.next
                else:
                    curr = curr.next
                peek = peek.next
        if duplicated:
            curr.next = curr.next.next
        return dummy.next
# @lc code=end
# %%
