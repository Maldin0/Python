'''PSCP Program'''
def main(txt):
    '''8432-Digit v2 04/11/2022'''
    if txt.count('thousand') > 0:
        print(4)
        return
    elif txt.count('hundred') > 0:
        print(3)
        return
    for i in ('ten', 'eleven', 'twelve', 'teen', 'ty'):
        if i in txt:
            print(2)
            return
    print(1)

main(input())
