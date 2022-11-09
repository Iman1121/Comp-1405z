def largest_prime_factor(n):
    factors = [i for i in range(1,n+1) if n%i == 0]
    prime_factors = [1]
    for x in factors:
        factors_2 = [i for i in range(1,x+1) if x%i == 0]
        if(len(factors_2) == 2):
            prime_factors.append(x)
    return max(prime_factors)
print(largest_prime_factor(1))


