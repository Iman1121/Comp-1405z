def get_number_purchases(data):
    count = 1
    purchases = 0
    file = open(data,"r")
    line = file.readline()
    while line != "":
        if(count == 6):
            purchases = purchases + 1
            count = 1
        else:
            count = count + 1
        line = file.readline() 
    return purchases

def get_total_purchases(data):
    count = 1
    
    price = 0
    file = open(data,"r")
    line = file.readline()
    while line!= "":
        if(count == 6):
            price = price + int(line)
            count = 1
        else:
            count = count+1
        line = file.readline()
    return price

def get_average_purchases(data):
    return round(get_total_purchases(data)/get_number_purchases(data),2)

def get_number_customer_purchases(data, name):
    file = open(data,"r")
    purchases = 0
    line = file.readline()
    while line != "":
        if(line == name + "\n"):
            purchases = purchases + 1
        line = file.readline()
    return purchases

def get_total_customer_purchases(data, name):
    file = open(data,"r")
    price = 0
    line = file.readline()
    while line != "":
        if(line == name + "\n"):
            for x in range(5):
                line = file.readline()
            price = price +int(line)    
        line = file.readline()
    return price

def get_average_customer_purchases(data, name):
    answer = get_number_customer_purchases(data,name)
    if(answer == 0):
        return 0
    return get_total_customer_purchases(data,name)/answer


def get_most_popular_product(data):
    count = 1
    desktop = 0
    laptops = 0
    tablet = 0
    toaster = 0
    file = open(data,"r")
    line = file.readline()
    while line != "":
        if(count == 6 or count >6):
            count = 0
        if(count == 2 ):
            desktop = desktop + int(line)
        elif(count == 3):
            laptops = laptops + int(line)
        elif(count == 4):
            tablet = tablet + int(line)
        elif(count == 5):
            toaster = toaster + int(line)
        count = count + 1
        line = file.readline()   
    if(desktop > toaster and desktop > laptops and desktop > tablet):
        popular = "Desktop"
    elif(toaster>laptops and toaster>tablet):
        popular = "Toaster"
    elif(laptops > tablet):
        popular = "Laptops"
    else:
        popular = "Tablet"
    return popular





