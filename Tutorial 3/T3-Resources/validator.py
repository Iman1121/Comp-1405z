import mystack

def isvalid(string):
    stack= []
    for x in string:
        if(x=="{" or x == "[" or x == "("):
            mystack.push(stack,x)
        elif(x == "}" or x == "]" or x == ")"):
            if(mystack.peek(stack) == "(" and x == ")"):
                mystack.pop(stack)
            elif(mystack.peek(stack) == "{" and x == "}"):
                mystack.pop(stack)
            elif(mystack.peek(stack) == "[" and x == "]"):
                mystack.pop(stack)
            elif(mystack.isempty(stack)):
                return False
            else:
                return False
    if(mystack.isempty(stack)):
        return True
    else:
        return False



         
            

