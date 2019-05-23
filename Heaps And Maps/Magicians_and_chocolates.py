# Given N bags, each bag contains Ai chocolates. There is a kid and a magician. In one unit of time, kid chooses a random bag i, eats Ai chocolates, then the magician fills the ith bag with floor(Ai/2) chocolates.

# Given Ai for 1 <= i <= N, find the maximum number of chocolates kid can eat in K units of time.

# For example,

# K = 3
# N = 2
# A = 6 5

# Return: 14
# At t = 1 kid eats 6 chocolates from bag 0, and the bag gets filled by 3 chocolates
# At t = 2 kid eats 5 chocolates from bag 1, and the bag gets filled by 2 chocolates
# At t = 3 kid eats 3 chocolates from bag 0, and the bag gets filled by 1 chocolate
# so, total number of chocolates eaten: 6 + 5 + 3 = 14

# Note: Return your answer modulo 10^9+7
def buildHeap(arr,n):
    for i in range(n//2,-1,-1):
        heapifyDown(arr,i,n)
    
def heapifyDown(arr,i,n):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if (left<n and arr[left]>arr[largest]):
        largest = left
    if right<n and arr[right]>arr[largest]:
        largest = right
    if largest!=i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapifyDown(arr,largest,n)

def nchoc(self, A, B):
    n = len(B)
    buildHeap(B,n)
    time=  0
    res=0
    while time!=A:
        res += B[0]
        B[0]=B[0]//2
        heapifyDown(B,0,n)
        time+=1
    res = res%1000000007
    return res

print(nchoc("",5,[6]))
