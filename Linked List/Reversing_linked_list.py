def reverseList(self, A):
    if A==None:
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

    
