'''PSCP Program'''
def main():
    '''8351-3nPlus1 21/10/2022'''
    while True:
        number, count = int(input()), 0
        if number == 0:
            break
        while True:
            if number == 1:
                print(count + 1)
                break
            if not number % 2:
                number /= 2
            else:
                number = number * 3 + 1
            count += 1

main()
