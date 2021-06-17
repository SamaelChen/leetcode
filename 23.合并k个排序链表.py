#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if not l1:
#             return l2
#         if not l2:
#             return l1
#         if l1.val > l2.val:
#             l2.next = self.mergeTwoLists(l1, l2.next)
#             return l2
#         else:
#             l1.next = self.mergeTwoLists(l1.next, l2)
#             return l1
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         if len(lists) == 0:
#             return None
#         if len(lists) == 1:
#             return lists[0]
#         res = lists[0]
#         for l2 in lists[1:]:
#             res = self.mergeTwoLists(res, l2)
#         return res


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
# @lc code=end

