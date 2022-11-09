def analyze(data):
    file = open(data,"r")
    line = file.readline()
    count = 0
    streak = []
    while line!="":
        if(int(line)%2 == 1):
            count += 1
        elif(int(line)%2 == 0):
            streak.append(count)
            count = 0
        line = file.readline()
    streak.append(count)
    return max(streak)

