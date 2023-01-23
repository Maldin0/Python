'''PSCP Program'''
def main(number, count):
    '''8358-SqFree 22/10/2022'''
    for i in range(1, number+1):
        if sqfree(i):
            count += 1
    print(count)

def sqfree(var_i):
    '''Square free algorithm?'''
    if var_i % 2 == 0:
        var_i = var_i / 2
    if var_i % 2 == 0:
        return False
    for j in range(3, int(var_i**0.5 + 1)):
        if var_i % j == 0:
            var_i = var_i / j
        if var_i % j == 0:
            return False
    return True
main(int(input()), 0)
