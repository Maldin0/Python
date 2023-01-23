'''PSCP Program'''
def main(number, total):
    '''8363-CircularPrime 23/10/2022'''
    if number < 11:
        for i in range(2, number+1):
            if isprime(i):
                total.append(i)
    else:
        total = [2, 3, 5, 7]
        for i in range(11, number+1):
            temp = i
            flag = True
            for _ in range(len(str(i))):
                if not isprime(int(temp)):
                    flag = False
                    break
                temp = str(temp)[1:] + str(temp)[0]
            if flag:
                total.append(i)
    print(sum(total))

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

main(int(input()), [])
    