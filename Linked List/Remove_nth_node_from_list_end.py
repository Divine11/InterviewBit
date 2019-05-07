# Given a linked list, remove the nth node from the end of list and return its head.

# For example,
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.

#  Note:
# If n is greater than the size of the list, remove the first node of the list.
# Try doing it using constant additional space.
def removeNthFromEnd(A,B):
    #Calculating length
    temp = A
    lenA = 0
    while temp:
        lenA+=1
        temp = temp.next
    if lenA==0:
        return A
    if B==0:
        diff = lenA-1
        temp = A
        while diff>0:
            temp = temp.next
            diff-=1
        temp.next = None
        return A
    if B>=lenA:
        A = A.next
        return A
    else:
        diff = lenA-B-1
        temp=A
        while diff>0:
            temp = temp.next
            diff-=1
        to_delete = temp.next
        temp.next = to_delete.next
        return A
