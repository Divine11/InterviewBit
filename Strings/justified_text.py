def fullJustify(A,B):
    cur_word_len = 0
    cur_word = []
    result = []
    i = 0
    while i<len(A):
        if cur_word_len+len(A[i])>B or (B-(cur_word_len+len(A[i]))<len(cur_word)):
            slots = len(cur_word)-1
            if slots==0:
                result.append("".join(cur_word)+" "*(B-cur_word_len))
            else:
                remaining = B-cur_word_len
                j=0
                k=0
                temp = ""
                while j<remaining:
                    cur_word[k] = cur_word[k]+" "
                    k = (k+1)%slots
                    j+=1
                result.append("".join(cur_word))
            cur_word = []
            cur_word_len = 0
        else:
            cur_word_len += len(A[i])
            cur_word.append((A[i]))
            i+=1
    if cur_word_len!=0:
        temp = " ".join(cur_word)
        result.append(temp+(" "*(B-len(temp))))
    print(*result,sep='\n')
    #return result

A = ["am", "fasgoprn", "lvqsrjylg", "rzuslwan", "xlaui", "tnzegzuzn", "kuiwdc", "fofjkkkm", "ssqjig", "tcmejefj", "uixgzm", "lyuxeaxsg", "iqiyip", "msv", "uurcazjc", "earsrvrq", "qlq", "lxrtzkjpg", "jkxymjus", "mvornwza", "zty", "q", "nsecqphjy" ]
B = 14
fullJustify(A,B)
    
    
            

