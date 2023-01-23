'''PSCP Program'''
def main(primes, target, count):
    '''8383-Semi Prime 06/11/2022'''
    for i in range(1, int((target//2)+1)):
        if isprime(i):
            primes.append(i)
    primes_copy = primes.copy()
    for i in primes:
        for j in primes_copy:
            if i*j <= target:
                count += 1
        primes_copy.pop(0)
    print(count)

def isprime(num):
    """Check for prime"""
    if num in (2, 3):
        return True
    if num % 2 == 0 or num < 2:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

main([], int(input()), 0)
