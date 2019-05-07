# Given a linked list, swap every two adjacent nodes and return its head.

# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
def swapPairs(self,A):
    if A==None or A.next==None:
        return
    start = A
    prev = None
    while start and start.next:
        a = start
        b = start.next
        if prev==None:
            A = b
        else:
            prev.next = b
        a.next = b.next
        b.next = a
        start = a.next
        prev = a
    return A
        