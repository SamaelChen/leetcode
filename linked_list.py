# %%
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# %%
def generateLN(lst):
    if len(lst) == 0:
        return None
    else:
        for idx, x in enumerate(lst):
            curr = ListNode(x)
            if idx == 0:
                node = curr
                head = node
            else:
                node.next = curr
                node = node.next
    return head
# %%
lst = [1,2,3,4,5]
ln = generateLN(lst)
# %%
class ReverseList:
    def __init__(self):
        self.remain = None


    def reverseList(self, head):
        if head.next is None or head is None:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last


    def reverseTopN(self, head, n):
        if head.next is None or head is None:
            return head
        if n == 1:
            self.remain = head.next
            return head
        last = self.reverseTopN(head.next, n-1)
        head.next.next = head
        head.next = self.remain
        return last

    
    def reverseBetween(self, head, left, right):
        if left == 1:
            return self.reverseTopN(head, right)
        head.next = self.reverseBetween(head.next, left-1, right-1)
        return head


    def reverseSE(self, head, rightnode):
        if head.next == rightnode:
            self.remain = head.next
            return head
        last = self.reverseSE(head.next, rightnode)
        head.next.next = head
        head.next = self.remain
        return last


    def reverseKGroup(self, head, k):
        if head is None:
            return head
        a = b = head
        for _ in range(k):
            if b is None:
                return head
            b = b.next
        last = self.reverseSE(a, b)
        a.next = self.reverseKGroup(b, k)
        return last

# %%
lst = [1, 2, 3, 4, 5, 6]
ln = generateLN(lst)
s = ReverseList()
a = s.reverseList(ln)
while a is not None:
    print(a.val)
    a = a.next
# %%
lst = [1, 2, 3, 4, 5, 6]
ln = generateLN(lst)
s = ReverseList()
a = s.reverseTopN(ln, 2)
while a is not None:
    print(a.val)
    a = a.next
# %%
lst = [1, 2, 3, 4, 5, 6]
ln = generateLN(lst)
s = ReverseList()
a = s.reverseBetween(ln, 2, 4)
while a is not None:
    print(a.val)
    a = a.next
# %%
lst = [1, 2, 3, 4, 5, 6]
ln = generateLN(lst)
s = ReverseList()
a = s.reverseSE(ln, None)
while a is not None:
    print(a.val)
    a = a.next
# %%
lst = [1, 2, 3, 4, 5, 6]
ln = generateLN(lst)
s = ReverseList()
a = s.reverseKGroup(ln, 4)
while a is not None:
    print(a.val)
    a = a.next

# %%
def reverse(a, b):
    if a is None:
        return a
    pre = None
    curr = a
    nxt = a
    while curr != b:
        nxt = curr.next
        curr.next = pre
        pre = curr
        curr = nxt
    return pre

def reverseKGroup(head, k):
    if head is None:
        return head
    a = b = head
    while b is not None:
        for _ in range(k):
            if b is None:
                return
            b = b.next
        r = reverse(a, b)
        r.next = b
        a = b
    return r

# %%
lst = [1, 2, 3, 4, 5, 6]
ln = generateLN(lst)
a = reverseKGroup(ln, 2)
while a is not None:
    print(a.val)
    a = a.next
# %%
