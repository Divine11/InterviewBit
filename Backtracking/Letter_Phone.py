# Given a digit string, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below.



# The digit 0 maps to 0 itself.
# The digit 1 maps to 1 itself.

# Input: Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Make sure the returned strings are lexicographically sorted.

def letterCombinationUtil(A,B,C,Mapping):
    if len(A)==0:
        return
    for i in range(len(A)):
        for j in range(len(Mapping[A[i]])):
            B.append(Mapping[A[i]][j])
            letterCombinationUtil(A[i+1:],B,C,Mapping)
            B.pop()



def letterCombinations(A):
    Mapping = dict()
    Mapping["1"] = "1"
    Mapping["2"] = "abc"
    Mapping["3"] = "def"
    Mapping["4"] = "ghi"
    Mapping["5"] = "jkl"
    Mapping["6"] = "mno"
    Mapping["7"] = "pqrs"
    Mapping["8"] = "tuv"
    Mapping["9"] = "wxyz"
    Mapping["0"] = "0"
    C = []
    letterCombinationUtil(A,[],C,Mapping)

letterCombinations("23")

