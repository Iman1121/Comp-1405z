import merge

def median_word_length(filename):
    word_length = []
    file = open(filename, "r")
    line = file.readline().split()
    for x in line: 
        word_length.append(len(x))
    mid =(0+len(word_length)-1)//2
    word_length = merge.merge_sort((word_length))

    if len(word_length)%2 == 0: 
        
        return (word_length[mid] + word_length[mid+1])/2
    else:
        
        return word_length[mid]
    

print(median_word_length("problem1-example-input.txt"))