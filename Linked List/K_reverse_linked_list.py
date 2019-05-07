# Given a singly linked list and an integer K, reverses the nodes of the

# list K at a time and returns modified linked list.

#  NOTE : The length of the list is divisible by K 
# Example :

# Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,

# You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5

# Try to solve the problem using constant extra space.
# def reverseList(self, A, B):
#     count = 1
#     temp = A
#     if B<2:
#         return A
#     orig_head = A
#     start = orig_head
#     end = orig_head
#     cur = orig_head
#     group_last = None
#     while cur:
#         count+=1
#         cur = cur.next
#         if count%B==0:
#             pass
from LinkedList import ListNode
def reverseList(A,B):
    if B<2:
        return A
    prev = None
    count = 1
    temp = A
    start = A
    lenA = 0
    temp = A
    while temp!=None:
        temp = temp.next
        lenA+=1
    temp=A
    while temp and count<lenA:
        count+=1
        temp = temp.next
        if count%B==0:
            if prev==None:
                A,prev = reverseListPart(start,B)
            else:
                g,h  = reverseListPart(start,B)
                prev.next = g
                prev = h
            start = prev.next
            #print(temp.val,count)
            #printList("inside List reversing Part before while",A)
    return A


def reverseListPart(A,count):
    if A==None:
        return A
    lenA = 0
    temp = A
    while temp!=None:
        temp = temp.next
        lenA+=1
    
    if lenA==1:
        return A

    prev = None
    cur = A
    nex = None
    co = 0
    print("inside List reversing Part before while")
    # printList("inside List reversing Part before while",A)
    while cur!=None and co<count:
        nex = cur.next
        cur.next = prev
        prev = cur
        cur = nex
        co+=1
    if co>=count:
        A = prev
        while prev.next != None:
            prev = prev.next
        prev.next = cur
    print("inside List reversing Part after while")
    # printList("inside List reversing Part after while",A)
    return A,prev

def printList(self,A):
    temp = A
    while temp!=None:
        print(temp.val,"->",end=" ")
        temp = temp.next
    print()

A = ListNode(1)
A.next = ListNode(2)
A.next.next = ListNode(3)
A.next.next.next = ListNode(4)
A.next.next.next.next = ListNode(5)
A.next.next.next.next.next = ListNode(6)


printList("s",A)
A = reverseList(A,2)
printList("s",A)
