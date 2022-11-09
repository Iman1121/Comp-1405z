import crawler
import os
import math
def get_outgoing_links(URL):
    
    links = []
    title = crawler.grab_title(URL)
    if(title == None):
        return None
    fileout = open(os.path.join("crawler", title, "outgoing.txt"), "r")
    x = fileout.readline().strip()
    while x != "":
        links.append(x)
        x = fileout.readline().strip()
    fileout.close()
    return links

def get_incoming_links(URL):
    links = []
    title = crawler.grab_title(URL)
    if(title == None):
        return None
    fileout = open(os.path.join("crawler", title, "incoming.txt"), "r")
    x = fileout.readline().strip()
    while x != "":
        links.append(x)
        x = fileout.readline().strip()
    fileout.close()
    return links

def get_page_rank(URL):
    title = crawler.grab_title(URL)
    
    if (title == None or os.path.isfile(os.path.join("crawler", "idf_values", "page_rank", title)) == False):
        return -1
    else:
        fileout = open(os.path.join(os.path.join("crawler", "idf_values", "page_rank", title)))
        x = fileout.readline().strip()
        fileout.close()
        print("hi")
        return float(x)
    
    

def get_idf(word):
    if os.path.isfile(os.path.join("crawler", "idf_values", word)):
        fileout = open(os.path.join("crawler", "idf_values", word), "r")
        x = fileout.readline()
        fileout.close()
    else:
        return 0
    return float(x)

def get_tf(URL, word):
    title = crawler.grab_title(URL)
    if(title == None):
        return 0
    if os.path.isfile(os.path.join("crawler", title, "tf_values", word)):
        fileout = open(os.path.join("crawler", title, "tf_values", word), "r")
        x = fileout.readline()
        fileout.close()
    else:
        return 0
    return float(x)

def get_tf_idf(URL, word):
    title = crawler.grab_title(URL)
    if(title == None):
        return 0
    if os.path.isfile(os.path.join("crawler", title, "idf_tf_values", word)):
        fileout = open(os.path.join("crawler", title, "idf_tf_values", word), "r")
        x = fileout.readline()
        fileout.close()
    else:
        return 0
    return float(x)

#crawler.crawl("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html")
#print(get_page_rank("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html"))
# print(get_incoming_links("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html"))