'''PSCP Program'''
def main(set_of_nums, size):
    ''' Tuple's Sad life '''
    size_real = tuple(set_of_nums.split())
    # print(size_real)
    temp = ''
    if size_real == 0:
        print(0)
    else:
        for _ in range(size_real.count(size)):
            for _ in range(size_real.count(size)):
                temp += str(size_real.index(size)) + ' '
            print(temp.rstrip())
            temp = ''
# 0
# 1 1
# 1 1
# 2 2 2
# 2 2 2
# 2 2 2
main(input(), input())
