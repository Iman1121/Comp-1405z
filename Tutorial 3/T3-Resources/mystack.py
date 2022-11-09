def push(stack, value):
    stack.append(value)

def pop(stack):
    if(len(stack)>0):
        return stack.pop()
    else:
        return None

def isempty(stack):
    if(len(stack)==0):
        return True
    else:
        return False

def peek(stack):
    if(len(stack)>0):
        return stack[len(stack)-1]
    else:
        return None
