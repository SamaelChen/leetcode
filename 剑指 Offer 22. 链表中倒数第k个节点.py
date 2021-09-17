# %%
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast, slow = head, head
        while fast and k > 0:
            fast = fast.next
            k -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        return slow


# %%
s = Solution()
l = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
res = s.getKthFromEnd(l, 2)
while res:
    print(res.val)
    res = res.next
# %%
