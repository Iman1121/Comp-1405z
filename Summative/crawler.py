import time
import webdev
import os
import math
#function for getting the title in a link, take split by \n list of html data or a url and returns the title

def produce_page_rank():

    #producing page ranks and saving them
    index_tracker = [] #contains all the files explored in the crawl and also the list used to track indexes in matrix
    files = os.listdir("crawler")
    for file in files:
        if(file == "idf_values"):
            pass
        else:
            index_tracker.append(file)
    
    
    adjacency = [] #creating empty matrix
    for x in range(len(index_tracker)):
        column = []
        for y in range(len(index_tracker)):
            column.append(0)
        adjacency.append(column)

    for file in files: 
        if(file == "idf_values"):
            pass
        else:
            fileout = open(os.path.join("crawler", file, "outgoing.txt"), "r")
            olinks = []
            x = fileout.readline().strip()
            while x != "":
                x = grab_title(x)
                olinks.append(x)
                x = fileout.readline().strip()
            fileout.close()

            for idx, link in enumerate(index_tracker):
                
                if(link in olinks):
                    adjacency[index_tracker.index(file)][idx] = 1

    for idx_x, x in enumerate(adjacency):
        div = adjacency[idx_x].count(1)
        for idx_y, y in enumerate(adjacency):
            if(adjacency[idx].count(0) == len(index_tracker)):
                adjacency[idx_x][idx_y] = 1/len(index_tracker)
            if(adjacency[idx_x][idx_y]==1):
                adjacency[idx_x][idx_y] = 1/div
            adjacency[idx_x][idx_y] = adjacency[idx_x][idx_y]*0.9
            adjacency[idx_x][idx_y] = adjacency[idx_x][idx_y] + 0.1/len(index_tracker)
    
    ok1 = [[]]
    for k in range(len(index_tracker)):
        ok1[0].append(1/len(index_tracker))
    

    ok2 = mult_matrix(ok1, adjacency)
    ed = 0
    for idk, k in enumerate(ok1):
        ed = ed + (ok2[0][idk] - ok1[0][idk]) ** 2
    ed = math.sqrt(ed)
    while(ed >= 0.0001):
        ed = 0
        ok1 = ok2
        ok2 = mult_matrix(ok1, adjacency)
        for idk, k in enumerate(ok1):
            ed = ed + (ok2[0][idk] - ok1[0][idk]) ** 2
        ed = math.sqrt(ed)
    

    
        
    
    os.makedirs(os.path.join("crawler", "idf_values", "page_rank"))
    
    for idx, x in enumerate(index_tracker):
        fileout = open(os.path.join("crawler", "idf_values", "page_rank", x), "w")
        fileout.write(str(ok2[0][idx]))

def produce_store_idftf():
    #produces the idf tf values for each item in each link
    files = os.listdir("crawler")
    filesidf = os.listdir(os.path.join("crawler", "idf_values"))
    for file in files:
        if(file == "idf_values"):
            pass
        else:            
            os.makedirs(os.path.join("crawler", file, "idf_tf_values"))
            for x in filesidf:
                fileout = open(os.path.join("crawler", file, "idf_tf_values", x), "w")

                file_1 = open(os.path.join("crawler", "idf_values", x), "r")
                idf = float(file_1.readline().strip())
                file_1.close()         

                if os.path.isfile(os.path.join("crawler", file, "tf_values", x)):
                    file_1 = open(os.path.join("crawler", file, "tf_values", x), "r")
                    tf = float(file_1.readline().strip())
                    file_1.close()
                else:
                    tf = 0               
                fileout.write(str(math.log(1+tf,2)*idf))
                fileout.close()

def store_idf(all_words, all_titles):
    os.makedirs(os.path.join("crawler", "idf_values")) #calculates and stores idf
    for word in all_words:
        count = 0
        for title in all_titles:
            if os.path.isfile(os.path.join("crawler", title, "tf_values", word)):
                count += 1
        fileout = open(os.path.join("crawler", "idf_values", word), "w")
        fileout.write(str(math.log(len(all_titles)/(1+count),2)))
        fileout.close()

def store_outgoing(outgoing_links, title):
    fileout = open(os.path.join("crawler", title, "outgoing.txt"), "w") #stores outgoing links
    for x in outgoing_links:
        fileout.write(x +"\n")
    fileout.close()

def update_incoming(link, url):
    rlink = grab_title(link) #updates incoming links 
    if os.path.isdir(os.path.join("crawler", rlink)):
        pass
    else:
        os.makedirs(os.path.join("crawler", rlink))
    fileout = open(os.path.join("crawler", rlink, "incoming.txt"), "a")
    fileout.write(url +"\n")
    fileout.close

def relative_to_absolute(url, link):
    for idx,x in enumerate(url[::-1]):
        if(x=="/"):
            break
    return url[:-(idx+1)] + link[1:]

def find_tf(word, words, title):
    if os.path.isfile(os.path.join("crawler", title, "tf_values", word)):
        return None
    else:
        count = 0
        for y in words:
            if(y== word):
                count += 1
        fileout = open(os.path.join("crawler", title, "tf_values", word), "w")
        fileout.write(str(count/len(words)))
        fileout.close()

def mult_matrix(a, b):
    new_list = []
    for idx_x in range(len(a)):
        column = []
        for idx_y in range(len((b[0]))):
            column.append(0)
            for idx_z in range(len(b)):
                column[idx_y] += a[idx_x][idx_z] * b[idx_z][idx_y]
        new_list.append(column)
    return new_list

def grab_title(data):
    title = ""
    if(type(data) is str):
        data = webdev.read_url(data).split()
    for x in data:
        if("title" in x):            
            title = x[(x.index("<title>")+len("<title>")):x.index("</title>", (x.index("<title>")+len("<title>")))]
    if(title == ""):
        return None
    return title

def grab_link(element):
    return element[(element.index('href=\"')+len('href=\"')):element.index("\"", (element.index('href=\"')+len('href=\"')))]

#function for getting the words in link, takes split by \n list of html data and returns the data
def grab_words(data):
    words = []
    if(type(data) is str):
        data = webdev.read_url(data).split()
    for x in data:
        if("<p>" in x):
            start = data.index(x)
        if("</p>" in x):
            end = data.index(x)
            words = words + data[start+1:end]
    return words


def del_data(filepath):
    #deletes the crawler folder if it exists, the crawler folder contains all of our data
    # if (os.path.isdir(filepath)):
        files = os.listdir(filepath)
        for file in files:
            if (os.path.isdir(newFile:=os.path.join(filepath, file))):
                del_data(os.path.join(newFile))
            else:
                os.remove(os.path.join(newFile))

        os.rmdir(filepath)

 
def crawl(data):
    if (os.path.isdir("crawler")):
        del_data("crawler")          

    os.makedirs("crawler")#making main directory

    queue = [data]
    links = [data]
    all_words = []
    all_titles = []
    while (len(queue)>0):
        outgoing_links = []#resets outgoing links for each new link
        info = webdev.read_url(data).split() 
        title = grab_title(info) #grabs the title in the link
        words = grab_words(info) #grabs words in the link
        
        for word in words: #tracks all words that appear in crawl for idf
            if(word in all_words):
                pass
            else:
                all_words.append(word)

        if(title not in all_titles): #tracks all docs for idf
            all_titles.append(title)    

        
        
        if os.path.isdir(os.path.join("crawler", title)): #checks to see if the directory alrdy exists if not then it creates the directory
            pass
        else:
            os.makedirs(os.path.join("crawler", title))  
        

        fileout = open(os.path.join("crawler", title, "link"), "w") #stores link for final search function
        fileout.write(data)
        fileout.close

        if (os.path.isdir(os.path.join("crawler", title, "tf_values")) == False):
            os.makedirs(os.path.join("crawler", title, "tf_values")) #find tf and stores it for each word
        for word in words:
            find_tf(word, words, title)

        for element in info: #looking for outgoing links in the link
            if("href" in element): 
                collect_link = True
                
                # link = element[element.index("href"):].split("\"")[1]
                link = grab_link(element)
                
                if(link.startswith(".")): #checks if the link is a relative link and if it is convert to absolute
                    
                    link = relative_to_absolute(data, link)

                if link in links:
                    collect_link = False
                if(collect_link == True): #puts link in queue to be searched
                    links.append(link)
                    queue.append(link)      
                outgoing_links.append(link)

                update_incoming(link, data)
                
        store_outgoing(outgoing_links, title)

        data = queue.pop() #changes data to next link in queue
    
    store_idf(all_words, all_titles)

    produce_store_idftf()
    
    produce_page_rank()

    return len(links)


start = time.time()
print(crawl("http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html"))
#del_data("crawler")
# print(webdev.read_url("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html"))
# print(webdev.read_url("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html").split())
end = time.time()
print(end-start)


