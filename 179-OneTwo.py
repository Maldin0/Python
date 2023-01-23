'''PSCP Program'''
def main(var_n, var_s1, var_s2):
    '''8345-OneTwo 21/10/2022'''
    if var_n == 1:
        return var_s1
    if var_n == 2:
        return var_s2
    previous, previous_prev, temp = var_s2, var_s1, ''
    for _ in range(3, var_n+1):
        temp = previous + previous_prev
        previous_prev, previous = previous, temp
    return temp
print(main(int(input()), "1", '2'))
