def coldest_interval(tempratures, days):
    lowest_average = 30
    for idx, temperature in enumerate(tempratures):
        count = 0
        average = 0
        if(idx >= (days-1)):
            for x in range(days):
                average = average + tempratures[idx-x]
               
            count += 1
            average = average/days    
         
        
          
            if(average < lowest_average):
                lowest_average = average
    return lowest_average

print(coldest_interval([7, 6, -2, -6, -2, 0, -5, 10, -3, 10], 10))


