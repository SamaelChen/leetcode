#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
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
        post = []
        while curr is not None:
            curr.next, prev, curr = prev, curr, curr.next
        while prev is not None:
            post.append(prev.val)
            prev = prev.next
        return post

    def isPalindrome(self, head: ListNode) -> bool:
        curr = head
        pre = []
        while curr is not None:
            pre.append(curr.val)
            curr = curr.next
        post = self.reverseList(head)
        if pre == post:
            return True
        else:
            return False

# @lc code=end
