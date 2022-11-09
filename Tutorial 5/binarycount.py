def binarysearch(list ,value, start = 0, end = None):
    
    if(end == None):
        end = len(list)-1
    if start > end:
        return -1
    mid = (start+end)//2
    if(value == list[mid]):
        return mid
    elif(value > list[mid]):
        return binarysearch(list,value,mid+1,end)
    elif(value < list[mid]):
        return binarysearch(list,value, start,mid-1)

def findstart(list,value):
    idx = binarysearch(list,value)
    while(idx> 0 and list[idx] == list[idx-1]):
        idx -= 1
    return idx

def findend(list,value):
    idx = binarysearch(list,value)
    while(idx<len(list)-1 and list[idx] == list[idx+1]):
        idx += 1 
    return idx

def count(list,value):
    x = findend(list,value)
    y = findstart(list,value)
    if(x==-1 or y ==-1):
        return "Not in List"
    return x - y + 1
    
"""
1. My binary search is faster according to tests and theory

2. When you lower the list of numbers to search linear search become surperior to binary search. 
And as you increase the numbers to search through, binary search becomes significantly better than linear search.
For example when the list you are searching through only has 100 items. Linear search was 3 times faster than binary on my computer
But when the list has 50000 items. Binary search is 13 times faster

3. Doesn't change anything. Minor difference in times can occur because lists are randomly generated every time. Makes sense since linear search isn't looping through more or less numbers. 
Binary search might go through more or less loops to determine if there is more duplicates. But these extra steps are insignificant compared to the rest of the calculations.

4. Doesn't change anything. Minor difference in times can occur because lists are randomly generated every time.
Linear search is still going through each and every value in the list and binary search is still doing the same sequence to look for the number

5. yes it does make sense. Linear search is only fast when you are dealing with a small amount of numbers.
But for a huge amount of numbers, binary seach should be significantly faster as it can search through many numbers in only a couple of calculations.
"""

list = [1,2,2,3,4]
print(count(list,5))