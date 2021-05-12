#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        curr = head
        while curr is not None:
            curr.next = Node(curr.val, next=curr.next)
            curr = curr.next.next
        curr = head
        while curr is not None:
            if curr.random is not None:
                curr.next.random = curr.random.next
            curr = curr.next.next
        new = head.next
        o, n = head, new
        while n.next is not None:
            o.next = n.next
            n.next = n.next.next
            o = o.next
            n = n.next
        o.next = None
        return new
# @lc code=end

