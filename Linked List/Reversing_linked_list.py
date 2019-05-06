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
    nex = cur.next
    while cur!=None:
        cur.next = prev
        cur = nex
        prev = cur
        if cur!=None:
            nex = cur.next
    A = prev

    
