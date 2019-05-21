# ind shortest unique prefix to represent each word in the list.

# Example:

# Input: [zebra, dog, duck, dove]
# Output: {z, dog, du, dov}
# where we can see that
# zebra = z
# dog = dog
# duck = du
# dove = dov
#  NOTE : Assume that no word is prefix of another. In other words, the representation is always possible. 
class TrieNode: 
    # Trie node class 
    def __init__(self): 
        self.children = [None]*26
        self.isEndOfWord = False
        self.count = 0

def char_to_int(a):
    return ord(a)-ord('a')

def int_to_char(integer):
    return chr(integer+ord('a'))

def give_trie_node(lis):
    if len(lis)==0:
        return None
    root = TrieNode()
    cur = None
    for i in lis:
        cur = root
        for j in i:
            indx = char_to_int(j)
            if cur.children[indx]==None:
                cur.children[indx] = TrieNode()
            cur.count+=1
            cur = cur.children[indx]
        cur.isEndOfWord = True
    return root

def print_trie(root,A):
    if root.isEndOfWord:
        print("".join(A))
        return
    for i in range(26):
        if root.children[i]!=None:
            A.append(int_to_char(i))
            print_trie(root.children[i],A)
            A.pop()


#print_trie(p,[])
def prefix(self,A):
    root = give_trie_node(A)
    res = []
    for i in A:
        temp = root
        lis = []
        for j in i:
            indx = char_to_int(j)
            if temp.count==1:
                break
            else:
                temp = temp.children[indx]
            lis.append(j)
        res.append(''.join(lis))
    return res

print(prefix("",["zebra" ,"dog", "duck", "dove"]))

