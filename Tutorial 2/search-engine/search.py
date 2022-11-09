def search(data,word):
    file = open(data,"r")
    line = file.readline()
    count = 0
    word_count = 0
    while line != "":
        if(line == word+"\n"):
            word_count += 1
        line = file.readline()
        count += 1
    return word_count, word_count/count

search_word = input("Enter your search word: ")
pages = open("pages.txt","r").readlines()
word_count= []
ratios = []
count = 0
for page in pages:
    x,y = search(page.strip("\n"),search_word)
    word_count.append(x)
    ratios.append(y)

print("Max Page(Count):" + pages[word_count.index(max(word_count))])
print("Max Count:"+ str(max(word_count)) + "\n")
print("Max Page (Ratio): " + pages[ratios.index(max(ratios))])
print("Max Ratio: "+ str(max(ratios)) + "\n")

