# Reverse a linked list from position m to n. Do it in-place and in one-pass.

# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,

# return 1->4->3->2->5->NULL.

#  Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list. Note 2:
# Usually the version often seen in the interviews is reversing the whole linked list which is obviously an easier version of this question. 
def reverseBetween(self, A, B, C):
    before = ListNode(None)
    before.next = A
    temp = A
    for _ in range(B-1):
        before = before.next
        temp = temp.next
    firstToReverse = temp
    n = temp.next
    for _ in range(C-B):
        nn = n.next
        n.next = temp
        temp = n
        n = nn
    firstToReverse.next = n
    before.next = temp
    return A if B > 1 else before.next

