def getIntersectionNode(self, A, B):
        #print("call")
        lenA = 0
        temp = A
        while temp!=None:
            temp = temp.next
            lenA+=1
        lenB = 0
        temp = B
        while temp!=None:
            temp = temp.next
            lenB+=1
        #print(lenA,lenB)
        if lenA==0 or lenB==0:
            return None
        diff_len = abs(lenA-lenB)
        is_intersect = False
        temp1 = A
        temp2 = B
        if lenA>lenB:
            while diff_len>0:
                temp1 = temp1.next
                diff_len-=1
        elif lenA<lenB:
            while diff_len>0:
                temp2 = temp2.next
                diff_len-=1
        while temp1!=None and temp2!=None:
                if temp1 ==temp2:
                    return temp1
                temp1 = temp1.next
                temp2 = temp2.next
        return None