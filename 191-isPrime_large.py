'''PSCP Program'''
def main(num):
    '''8357-isPrime_large 21/10/2022'''
    print('YES' if isprime(num) and num > 1 else 'NO')
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
main(int(input()))
