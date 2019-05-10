# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Examples:

#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

def evalRPN(A):
    n = len(A)
    expresssion = ["+","-","*","/"]
    if n==1:
        return A[0]
    else:
        stack = []
        for i in A:
            if i not in expresssion:
                stack.append(i)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                inde = expresssion.index(i)
                if inde==0:
                    stack.append(b+a)
                elif inde==1:
                    stack.append(b-a)
                elif inde==2:
                    stack.append(b*a)
                else:
                    stack.append(b//a)
        return stack[-1]

print(evalRPN(["4", "13", "5", "/", "+"]))