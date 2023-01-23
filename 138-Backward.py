'''PSCP Program'''
def main():
    '''Backward'''
    data = []
    while True:
        text = input()
        if text == "NULL":
            break
        data.append(text)
    print(*reversed(data), sep='\n')
main()

