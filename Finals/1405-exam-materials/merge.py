def merge_sort(mylist):
    if len(mylist) == 1:
        return mylist
    left = merge_sort(mylist[0:int(len(mylist)/2)])
    right = merge_sort(mylist[int(len(mylist)/2):len(mylist)])
    return merge(left, right)
    

def merge(left, right):
    left_index = 0
    right_index = 0
    result = []

    

    while len(result) < len(left) + len(right): 
        if left_index >= len(left): 
            result.append(right[right_index])
            right_index += 1
        elif right_index >= len(right):
            result.append(left[left_index])
            left_index += 1
        elif left[left_index] < right[right_index]:
            
            result.append(left[left_index])
            left_index += 1
        else:
            
            result.append(right[right_index])
            right_index += 1

    return result