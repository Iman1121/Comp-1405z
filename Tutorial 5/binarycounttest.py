import random
import time
import binarycount

search = []
searchin = []

for i in range(2500):
    searchin.append(random.randint(0,1000))

for i in range(50000):
    search.append(random.randint(0,10000))

searchin.sort()
count = 0
start = time.time()

for value in search:
    binarycount.count(searchin,value)
end = time.time()
print("Binary: " + str(end-start))


start = time.time()
for value in search:
    searchin.count(value)
end = time.time()
print("Linear: " + str(end-start))