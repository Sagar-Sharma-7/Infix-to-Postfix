# Infix to postfix

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numbers = "0123456789"

open_b = "("
close_b = ")"
operations = "+-*/"
stack = []
z = ""
x = "(( A + B ) + C)"

def postfix(stack, z, x):
    for i in range(len(x)):
        if x[i] == "(":
            stack.append(x[i])
            continue
        elif x[i] in [*alphabets]:
            z += x[i]
        elif x[i] in [*operations]:
            stack.append(x[i])
        elif x[i]  == ")":
            print(stack)
            while True:
                w = str(stack.pop())
                if w != "(":
                    z += w 
                else: break
        else: 
            continue
    print(z)
    print(stack)

postfix(stack, z, x)

