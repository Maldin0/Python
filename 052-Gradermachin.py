'''Runner'''
def rep(num1, num2):
    '''Repeat what i said'''
    text = "pass :"
    total = 0
    if num1 > num2:
        if num2%1 == 0:
            num1 += 2
        for i in range(num2, num1):
            if i%2 == 0:
                total += i
                text = text+" " +str(num1-i)
    elif num1 < num2:
        if num2%2 == 0:
            num2 += 2
        for i in range(num1, num2):
            if i%2 == 0:
                total += i
                text = text+" " +str(i)
    elif num1 == num2:
        total = num1
        text = text+" "+str(num1)
    print(text)
    print("Sum : %d" %total)
rep(int(input()), int(input()))
