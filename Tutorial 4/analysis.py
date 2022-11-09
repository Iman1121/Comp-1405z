def load(data):
    global list
    global count_unique
    global common_word
    global common_pair
    common_word = {}
    common_pair = {}
    count_unique = []
    file = open(data,"r")
    list = file.readline().strip().split() 
    for x in list:
        if(x not in count_unique):
            count_unique.append(x)    
    file.close()

def commonword(the_list):
    common_word = {}
    x =[x for x in the_list if x not in list]
    if((len(the_list)== 0) or (len(x)== len(the_list))):
        return None

    for x in the_list:
        count = 0
        for y in list:
            if(x==y):
                count += 1
        common_word.update({x:count})    
    return max(common_word, key =common_word.get)   

def commonpair(str):
    common_pair = {}
    if(str not in list):
        return None
    for idx_x, x in enumerate(list):
        if(idx_x + 1 == len(list)):
            pass  
        elif(x == str):
            if(list[idx_x+1] in common_pair):
                common_pair[list[idx_x+1]] += 1
            else:
                common_pair.update({list[idx_x+1]:0})
    
            
    return max(common_pair, key =common_pair.get)     

def countall():
    return len(list)

def countunique():      
    return len(count_unique)
