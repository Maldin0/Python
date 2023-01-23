'''PSCP Program'''
def main(num):
    '''8342-Fibonnaci 21/10/2022'''
    print(fibbo(num))
def fibbo(num):
    '''find fibbonaci'''
    return 1 if num == 1 else 0 if num == 0 else fibbo(num - 1) + fibbo(num - 2)

main(int(input()))
