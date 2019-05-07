# Given a list, rotate the list to the right by k places, where k is non-negative.

# For example:

# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.
def rotateRight(self, A, B):
    if A==None or A.next==None:
        return A
    lenA = 0
    temp = A
    while temp:
        lenA+=1
        temp=temp.next
    B = B%lenA
    if B==0:
        return A
    part1 = A
    part2 = A
    diff = lenA-B
    while diff>0:
        dif-=1
        part2 = part2.next
    A = part2
    while part2.next:
        part2 = part2.next
    part2.next = part1
    while part1.next!=A:
        part1 = part1.next
    part1.next = None
    return A