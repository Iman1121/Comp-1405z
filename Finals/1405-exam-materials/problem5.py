def box_weight(box):
    weight = 0
    for element in box:
        print(element)
        if(type(element) is list):
            print("i")
            weight+= box_weight(element)
        else:
            weight+=element
        
    return weight

