'''PSCP Program'''
def main():
    '''Cat Parade'''
    data = []
    while True:
        cat = input()
        if cat == "IT'S A DOG":
            data.pop()
        elif cat == 'END':
            break
        else:
            data.extend(cat.split(', '))
    for j in sorted(set(data)):
        print(j, data.index(j)+1, data.count(j))

main()
