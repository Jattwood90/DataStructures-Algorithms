# Parentheis stack problem - you may be asked to create a stack using class, however it is doable using lists and its methods as a function.

def balance(s):
    if len(s) %2 !=0:
        return False
    # edgecase check
    
    opening = set('[{(')
    matches = set( [('(',')'),('[',']'),('{','}')] )
    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:

            if len(stack) == 0:
                return False
            # edge case check

            last_open = stack.pop()
            # as soon as there is a closing parenthesis, it must match the first one, or else the
            # the stack is not balanced

            if (last_open, paren) not in matches:
                return False
    return len(stack) ==0



print(balance('({)'))
print(balance('{[}]'))
