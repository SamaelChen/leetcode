#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        lst = []
        while head is not None:
            lst.append(head.val)
            head = head.next
        lst.sort()
        newhead = curr = ListNode()
        for ele in lst:
            curr.next = ListNode(ele)
            curr = curr.next
        return newhead.next
# @lc code=end

