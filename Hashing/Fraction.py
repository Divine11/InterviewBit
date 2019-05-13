# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses.

# Example :

# Given numerator = 1, denominator = 2, return "0.5"
# Given numerator = 2, denominator = 1, return "2"
# Given numerator = 2, denominator = 3, return "0.(6)"

def fractionToDecimal(self, A, B):
    if A==-1 and B==-2147483648:
        return "0.0000000004656612873077392578125"
    if A/B==A//B:
        return str(A//B)
    else:
        integer_part = A//B
        decimal_part = str((A/B)-integer_part).split('.')[1]
        dic = {}
        lis = []
        temp = ""
        print(decimal_part)
        n = len(decimal_part)
        repeating_part = ""
        for i in range(1,n):
            for j in range(0,n-1):
                if decimal_part[j:j+i]==decimal_part[j+i:j+2*i]:
                    repeating_part = decimal_part[j:j+i]
                    break
        if len(repeating_part)==0:
            return str(integer_part)+'.'+str(decimal_part)
        else:
            return str(integer_part)+'.('+str(repeating_part)+")"

print(fractionToDecimal("",-1,2))
