# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

# For example, given following linked lists :

#   5 -> 8 -> 20 
#   4 -> 11 -> 15
# The merged list should be :

# 4 -> 5 -> 8 -> 11 -> 15 -> 20
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

def mergeTwoLists(self,A,B):
    if A==None:
        return B
    if B==None:
        return A
    C = None
    Res = None
    if A.val>B.val:
        C = ListNode(B.val)
        B = B.next
    else:
        C = ListNode(A.val)
        A = A.next
    Res = C
    while A and B:
        if A.val>B.val:
            C.next = ListNode(B.val)
            B = B.next
        else:
            C.next = ListNode(A.val)
            A = A.next
        C = C.next
    while A:
        C.next = ListNode(A.val)
        A = A.next
        C = C.next
    while B:
        C.next = ListNode(B.val)
        B = B.next
        C = C.next
    return Res
    