factors = []

k = 600851475143
i = 1
while k > 1:
    if 600851475143 % i == 0:
        k /= i
        factors.append(i)
    i += 1

print(factors)