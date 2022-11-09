max_size = 10

def enqueue(queue, value):
    if (len(queue) < max_size):
        queue.append(value)
        return True
    else:
        return False

def dequeue(queue):
    if(len(queue)>0):
        return queue.pop(0)
    else:
        return None

def peek(queue):
    if(len(queue)>0):
        return queue[0]
    else:
        return None

def isempty(queue):
    if(len(queue)== 0):
        return True
    else:
        False

def multienqueue(queue, items):
    count = 0
    for x in items:
        item = x
        if(len(queue)<max_size):
            count += 1
            queue.append(x)
        else:
            break
    return count

def multidequeue(queue, number):
    new_list = []
    for i in range(number):
        if(len(queue)>0):
            new_list.append(queue.pop(0))
        else:
            break
    return new_list


