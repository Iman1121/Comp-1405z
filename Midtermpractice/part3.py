def sum_divisors():
    x = int(input("Enter your number: "))
    list_x = [i for i in range(1,x+1) if x%i == 0]
    return sum(list_x)
print(sum_divisors())
    