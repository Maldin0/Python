'''PSCP Program'''
from hashlib import sha512
def main(d_hash):
    '''8375-BreakPassword 28/10/2022'''
    for i in range(0, 100000):
        if hashing(str(i).zfill(5)) == d_hash:
            print(str(i).zfill(5))
            break

def hashing(nums):
    '''8374-Password 28/10/2022'''
    return sha512(nums.encode('utf-8')).hexdigest().upper()


main(input())
