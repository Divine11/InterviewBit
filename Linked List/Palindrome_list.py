# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None
def lPalin(self, A):
    if A==None or A.next==None:
        return 1
    lenA = 0
    temp = A
    while temp!=None:
        lenA+=1
        temp = temp.next
    if lenA==2:
        return 1 if A.next.val==A.val else 0
    middle = A
    prev_middle = None
    count = 0
    while count<(lenA//2):
        prev_middle = middle
        middle = middle.next
        count+=1
    if lenA&1==1:
        prev_middle = middle
        middle = middle.next
    prev_middle.next = self.reverseList(middle)
    middle = prev_middle.next
    while A and middle:
        if A.val!=middle.val:
            return 0
        A =A.next
        middle = middle.next
    return 1


def reverseList(self, A):
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
    while cur!=None:
        nex = cur.next
        cur.next = prev
        prev = cur
        cur = nex
    return prev

def printList(self,A):
    temp = A
    while temp!=None:
        print(temp.val,"->",end=" ")
        temp = temp.next
    print()
