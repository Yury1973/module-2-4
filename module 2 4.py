numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    k = 0
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            k = k + 1
    if is_prime and i > 1:
        primes.append(i)
    elif k != 0 and i > 1:
        not_primes.append(i)
print('Primes:', primes)
print('Not Primes:', not_primes)
