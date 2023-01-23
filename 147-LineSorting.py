'''PSCP Program'''
def main():
    '''Line Sorting'''
    data = []
    for _ in range(int(input())):
        data.append(input())
    data.sort(key=sorter)
    print(*data, sep='\n')

def sorter(txt):
    '''return length of txt'''
    return len(txt)
main()
