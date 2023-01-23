'''PSCP Program'''


def main(num, out):
    '''Calculator V2'''
    if num <= 9:
        if num <= 1:
            return 1
        return num * 2
    num_len = len(str(num))
    for i in range(num_len-1):
        out += int('9' + '0'*i) * (i+2)
    out += (num - int('9'*(num_len-1))) * (num_len+1)
    return out


print(main(int(input()), 0))
