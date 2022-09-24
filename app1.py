# program to reverse a string using stack
def pop(l):
    if l != []: return l.pop()
    else: return False

def push(l, ch):
    l.append(ch)

def reverseString(s): 
    stack = list() # empty stack
    for ch in s:
        push(stack, ch)

    reverse = ""
    while True:
        ch = pop(stack)
        if ch != False: reverse += ch
        else: break
    
    return reverse

string = input("Enter your string: ")
print("Reverse string: ", reverseString(string))