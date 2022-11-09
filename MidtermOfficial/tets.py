file = open("studentinfo1.txt","r")
line = file.readline().strip()
string = line
while line != "":
    line = file.readline()
    string = string + line
    string.strip("MaryAliaga")
print(string)