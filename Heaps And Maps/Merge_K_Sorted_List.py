# Merge k sorted linked lists and return it as one sorted list.

# Example :

# 1 -> 10 -> 20
# 4 -> 11 -> 13
# 3 -> 8 -> 9
# will result in

# 1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def buildHeap(arr,n):
    for i in range(n//2,-1,-1):
        heapifyDown(arr,i,n)
    
def heapifyDown(arr,i,n):
    left = 2*i+1
    right = 2*i+2
    smallest = i
    if (left<n and arr[left][0]<arr[smallest][0]):
        smallest = left
    if right<n and arr[right][0]<arr[smallest][0]:
        smallest = right
    if smallest!=i:
        arr[i],arr[smallest] = arr[smallest],arr[i]
        heapifyDown(arr,smallest,n)

def mergeKLists(self, A):
    k = len(A)
    root = None
    result_list = []
    current = None
    arr = []
    for i in range(k):
        arr.append([A[i].val,i])
    buildHeap(arr,len(arr))
    import sys
    inf = sys.maxsize
    z = 0
    while z!=k:
        val = arr[0][0]
        index = arr[0][1]
        if current==None:
            root = ListNode(val)
            result_list.append(val)
            current=root
        else:
            current.next = ListNode(val)
            result_list.append(val)
            current = current.next
        temp = A[index]
        if temp.next==None:
            arr[0][0] = inf
            heapifyDown(arr,0,k)
            z+=1
        else:
            temp = temp.next
            arr[0][0] = temp.val
            A[index] = temp
            heapifyDown(arr,0,k)
        print(arr)
    print(result_list)
    printLinkList(root)

def printLinkList(root):
    temp = root
    while temp:
        print(temp.val,"->",end=" ")
        temp = temp.next
# A = ListNode(1)
# A.next = ListNode(2)
# A.next.next = ListNode(3)
# A.next.next.next = ListNode(4)
# A.next.next.next.next = ListNode(5)

# C = ListNode(10)
# C.next = ListNode(45)
# C.next.next = ListNode(54)
# C.next.next.next = ListNode(59)
# C.next.next.next.next = ListNode(62)
# B = [C,A,ListNode(9),ListNode(11)]
# mergeKLists("",B)

# arr= [10,9,8,5,1,2,3,6]
# print(arr)
# buildHeap(arr,len(arr))
# print(arr)
# 10 9 8 20 38 44 55 65 66 79 87 2 68 72 5 5 55 61 73 89 2 30 73 4 28 73 84 96 3 54 82 83 5 15 33 38 94 100 1 4 5 22 32 42 64 86 2 11 78

def getList():
    k = int(input())
    res = []
    while k>0:
        arr = [int(x) for x in input().split()]
        root = ListNode(arr[1])
        current = root
        for i in arr[2:]:
            current.next = ListNode(i)
            current = current.next
        res.append(root)
        k-=1
    return res
mergeKLists("",getList())
