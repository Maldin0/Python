'''im dying'''
def plus():
    '''plus ultra'''
    stop = int(input())
    total = 0
    while True:
        num = int(input())
        if num == -1:
            break
        total += num
        if total == stop:
            break
    print(total)
plus()
