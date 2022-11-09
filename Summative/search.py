from operator import index
import os
import math
"""
get query
loop through query to get to find unique words
go through unique words and find their idftf
use idftfs to get vector
do vector calcs
"""
def get_query_idftf(word, word_count, length):
    if os.path.isfile(os.path.join("crawler", "idf_values", word)):
        fileout = open(os.path.join("crawler", "idf_values", word), "r")
        idf = float(fileout.readline().strip())
        fileout.close()
    else:
        idf = 0
    tf = word_count/length
    idf_tf = math.log((1+tf),2)*idf
    return idf_tf

def get_query_vector(u_words, length):
    vector = []
    index_key = []
    for word in u_words:
        append1 = get_query_idftf(word, u_words[word], length)
        vector.append(append1)
        index_key.append(word)
    
    return vector, index_key

def get_file_vector(file, index_key):
    vector = []
    for x in index_key:
        if os.path.isfile(os.path.join("crawler", file, "idf_tf_values", x)):
            fileout = open(os.path.join("crawler", file, "idf_tf_values", x), "r")
            idf_tf = float(fileout.readline().strip())
        else:
            idf_tf = 0
        vector.append(idf_tf)
    return vector

def cos_similarity(q_vector, f_vector):
    num = 0
    for x in range(len(q_vector)):
        num = num + (q_vector[x] * f_vector[x])
    qdem = 0
    for x in q_vector:
        qdem = qdem + x**2
    qdem = math.sqrt(qdem)
    fdem = 0
    for x in f_vector:
        fdem = fdem + x**2
    fdem = math.sqrt(fdem)
    if(fdem == 0 or qdem == 0):
        return 0
    return num/(fdem * qdem)

def content_score(query):
    words = query.split()
    length = len(words)
    u_words = {}
    list_of_tuple = []
    for word in words:
        if(word not in u_words):
            u_words.update({word:1})
        else:
            u_words[word] += 1
    q_vector, index_key = get_query_vector(u_words, length)
    files = os.listdir("crawler")
    for file in files:
        if(file == "idf_values"):
            pass
        else:
            f_vector = get_file_vector(file, index_key)
            cs = cos_similarity(q_vector, f_vector)
            cs_tuple = (file,cs)
            list_of_tuple.append(cs_tuple)
    list_of_tuple = sorted(list_of_tuple, key = lambda x:x[1])
    ranked_pages = []
    for x in range(10):
        x = list_of_tuple.pop()
        fileout = open(os.path.join("crawler", x[0], "link"), "r")
        url = fileout.readline().strip()
        my_dict = {
            "url": url,
            "title":x[0],
            "score":float(x[1])
        }
        ranked_pages.append(my_dict)
    return ranked_pages

def content_score_pagerank(query):
    words = query.split()
    length = len(words)
    u_words = {}
    list_of_list = []
    for word in words:
        if(word not in u_words):
            u_words.update({word:1})
        else:
            u_words[word] += 1
    q_vector, index_key = get_query_vector(u_words, length)
    files = os.listdir("crawler")
    for file in files:
        if(file == "idf_values"):
            pass
        else:
            f_vector = get_file_vector(file, index_key)
            cs = cos_similarity(q_vector, f_vector)
            cs_list = [file,cs]
            fileout = open(os.path.join("crawler", "idf_values", "page_rank", cs_list[0]), "r")
            x = float(fileout.readline().strip())

            cs_list[1] = cs_list[1] * x
            list_of_list.append(cs_list)
    list_of_list = sorted(list_of_list, key = lambda x:x[1])
    ranked_pages = []
    for x in range(10):
        x = list_of_list.pop()
        fileout = open(os.path.join("crawler", x[0], "link"), "r")
        url = fileout.readline().strip()
        my_dict = {
            "url": url,
            "title":x[0],
            "score":float(x[1])
        }
        ranked_pages.append(my_dict)
    return ranked_pages

def search(query, boost):
    if boost:
        return content_score_pagerank(query)
    else:
        return content_score(query)

#print(search("coconut fig cherry", True))



