'''PSCP Program'''
def main(times, count):
    '''8346-Divide3Or5 21/10/2022'''
    for i in range(1, times+1):
        if not i % 3 or not i % 5:
            count += i
    print(count)

main(int(input()), 0)
