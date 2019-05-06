# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Try solving it using constant additional space.

# Example :

# Input : 

#                   ______
#                  |     |
#                  \/    |
#         1 -> 2 -> 3 -> 4

# Return the node corresponding to node 3.
def detectCycle(self,A):
    if A==None or A.next==None:
            return None
    fast = A
    slow = A
    is_loop = False
    #print("Yolo",fast.next,slow,fast)
    while fast!=None and slow!=None and fast.next!=None:
        fast = fast.next.next
        slow = slow.next
        if fast==slow:
            is_loop = True
            break
        
    if not is_loop:
        return None
    else:
        slow = A
        while slow!=fast:
            slow = slow.next
            fast = fast.next
        return slow