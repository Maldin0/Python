'''Runner'''
def rep(num1, num2):
    '''Repeat what i said'''
    num = num1
    if num1 > num2:
        for _ in range(num2-1, num1):
            print(num)
            num -= 1
    else:
        for _ in range(num1-1, num2):
            print(num)
            num += 1
rep(int(input()), int(input()))

