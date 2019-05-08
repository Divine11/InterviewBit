# Sort a linked list in O(n log n) time using constant space complexity.

# Example :

# Input : 1 -> 5 -> 4 -> 3

# Returned list : 1 -> 3 -> 4 -> 5

def sorted_merge(A,B):
    res = None
    if A == None:
        return B 
    if B == None: 
        return A 
    if (A.val <= B.val): 
        res = A; 
        res.next = sorted_merge(A.next, B); 
    else:
        res = B; 
        res.next = sorted_merge(A, B.next);
    return res;

def sortList(self,A):
    if A==None or A.next==None:
        return A
    middle = self.getMiddle(A); 
    nextofmiddle = middle.next; 

    middle.next = None; 
    left = sortList(A); 
    right = sortList(nextofmiddle);

    sortedlist = sortList(left, right); 
    return sortedlist; 

def getMiddle(self,A):
    if A==None:
        return A
    fastptr = A.next
    slowptr = A
    while (fastptr != None): 
        fastptr = fastptr.next; 
        if (fastptr != None): 
            slowptr = slowptr.next; 
            fastptr = fastptr.next; 
    return slowptr;