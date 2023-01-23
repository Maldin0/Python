'''Huhu'''
def seq():
    '''seq'''
    text = []
    for i in range(int(input())):
        text.append((i+1)**2)
    print(*text, sep=" ")
seq()
