def is_prime(number):
    for i in range(2,int(number ** 1/2) + 1):
        if number % i == 0:
            return False
    return True

def count_primes(number):
    count = 0
    for i in range(2,number + 1):
        if is_prime(i):
            count += 1
    return count
print(count_primes(100))
