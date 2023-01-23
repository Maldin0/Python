'''PSCP Program'''
from hashlib import sha512
def main():
    '''8374-Password 28/10/2022'''
    temp = input().encode('utf-8')
    print(sha512(temp).hexdigest().upper())
main()
