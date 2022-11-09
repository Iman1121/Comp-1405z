def divisor():
    x = int(input("What is your first number? "))
    y = int(input("What is your second number? "))
    if(x == 0 or y == 0):
        return 0
    set_x = {i for i in range(1,x+1) if x%i == 0}
    set_y = {i for i in range(1,y+1) if y%i == 0}
    return max(set_x & set_y)
print(divisor())
        