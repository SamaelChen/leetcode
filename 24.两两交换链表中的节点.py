#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        l1 = ListNode(-1)
        count = 0
        target = 2
        p = l1
        while head and count < target:
            q = head
            head = head.next
            q.next = p.next
            p.next = q
            count += 1
            if count == target:
                while p.next:
                    p = p.next
                count = 0
        return l1.next
# @lc code=end

