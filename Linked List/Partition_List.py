# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5
from LinkedList import ListNode
def partition(A,B):
    first = A
    second = A
    first_back = None
    second_back = None
    while first:
        if first.val<B:
            if second_back==None and first_back==None:
                #print("yello")
                second_back = second
                second = second.next
                first_back = first
                first = first.next
            elif second_back==None:
                #print("yello1")
                first_back.next = first.next
                first.next = second
                A = first
                second_back = first
                first = first_back.next
            else:
                if second.val==first.val:
                    first_back = first
                    second_back = second
                    first = first.next
                    second = second.next
                else:
                    second_back.next = first
                    first_back.next = first.next
                    first.next = second
                    second_back = second_back.next
                    first = first_back.next
        else:
            first_back = first
            first = first.next
        
    return A

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
A = partition(A,6)
printList("s",A)

