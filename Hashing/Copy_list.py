# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or NULL.

# Return a deep copy of the list.

# Example

# Given list

#    1 -> 2 -> 3
# with random pointers going from

#   1 -> 3
#   2 -> 1
#   3 -> 1
# You should return a deep copy of the list. The returned answer should not contain the same node as the original list, but a copy of them. The pointers in the returned list should not link to any node in the original input list.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

def copyRandomList(self, head):
    if head==None:
        return None
    if head.next == None:
        clone_head =RandomListNode(head.label)
        clone_head.next = head.next
        if head.random == None:
            return clone_head
        else:
            clone_head.random = clone_head
            return clone_head
    
    cur = head
    clone_head = RandomListNode(cur.label)
    temp = clone_head
    cur = cur.next
    while cur!= None:        
        temp.next = RandomListNode(cur.label)
        cur = cur.next
        temp = temp.next
    
    cur = head
    temp = clone_head
    while cur!=None:
        next = cur.next
        cur.next = temp
        temp.random = cur
        temp = temp.next
        cur = next
    
    temp = clone_head
    cur = head
    while temp:
        if temp.random.random==None:
            temp.random = None
        else:
            temp.random = temp.random.random.next
        temp = temp.next
    
    return clone_head
    
    