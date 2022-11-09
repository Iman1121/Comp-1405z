
import merge


def most_common_colour(filename):
    file = open(filename, "r")
    count = 0
    line = file.readline().strip()
    colours = {}
    while line != "":
        count += 1
        line = file.readline().strip()

       
        if count == 3:
            if line in colours:
                colours[line] += 1
            else:
                colours.update({line: 1})

        if count == 5:
            count = 0
    return max(colours,key=colours.get)

def sorted_prices(filename):
    file = open(filename, "r")
    count = 0
    line = file.readline().strip()
    prices= []
    while line != "":
        count += 1
        line = file.readline().strip()
        if count == 4:
            price = line        
        elif (count == 5):
            if (line == "true"):
                
                prices.append(price)
                count = 0
            else:
                count = 0

    prices = merge.merge_sort(prices)[::-1]
    
    return prices[::-1]
