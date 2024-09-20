numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for j in numbers:
     if j < 2:
        continue
     is_primes = True
     for i in  range(2, j):
        if j % i == 0:
            not_primes.append(j)
            is_primes = False
            break
     if is_primes:
        primes.append(j)
         
print('Primes: ', primes)
print('Not Primes: ', not_primes)


