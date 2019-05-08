# Sort a linked list using insertion sort.

# We have explained Insertion Sort at Slide 7 of Arrays

# Insertion Sort Wiki has some details on Insertion Sort as well.
from LinkedList import ListNode
def insertionSortList(A):
    if A==None or A.next == None:
        return A
    current = res = ListNode(A.val)
    A = A.next
    while A:
        if current.val>A.val:
            head = res
            #it means node will come before head
            if head.val>A.val:
                temp = ListNode(A.val)
                temp.next = head
                res = temp
                A=A.next
            else:
                while head and head.next and head.next.val<A.val:
                    head = head.next
                temp = ListNode(A.val)
                temp.next = head.next
                head.next = temp
                A=A.next
        else:
            current.next = ListNode(A.val)
            current = current.next
            A = A.next
    return res
    

def printList(self,A):
    temp = A
    while temp!=None:
        print(temp.val,"->",end=" ")
        temp = temp.next
    print()
A = ListNode(5)
A.next = ListNode(4)
A.next.next = ListNode(3)
A.next.next.next = ListNode(5)
A.next.next.next.next = ListNode(1)
A.next.next.next.next.next = ListNode(4)


printList("s",A)
A = insertionSortList(A)
printList("s",A)

