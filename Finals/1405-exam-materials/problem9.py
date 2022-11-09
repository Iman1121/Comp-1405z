def sort_volumes(filename):
    file = open(filename, "r")
    line = file.readline().strip()
    count = 0
    volumes = []
    while line != "":
        count += 1
        if count == 1: 
            id = line
        elif count ==2:
            x = int(line)
        elif count == 3:
            y = int(line)
        elif count ==4:
            z = int(line)
            count = 0
            list = [id, x*y*z]
            volumes.append(list)
        line = file.readline().strip()
    
    return sorted(volumes, key = lambda x:x[1])