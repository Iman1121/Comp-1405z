def search(data):
    file = open(data,"r")
    line = file.readline()
    count = 0
    volumes = []
    while line!="":
        count += 1
        if count == 1:
            length = int(line.strip("\n"))
        elif count ==2:
            width = int(line.strip("\n"))
        elif count == 3:
            height = int(line.strip("\n"))
            count = 0
            volumes.append(height*length*width)
        line = file.readline()
    return max(volumes)

print(search("volumes4.txt"))
