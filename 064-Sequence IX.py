'''Sequence IX'''
def main():
    '''Sequence IX'''
    rows = int(input())
    k = 0
    count = 0
    count1 = 0
    for i in range(1, rows+1):
        for _ in range(1, (rows-i)+1):
            print("  ", end=" ")
            count += 1
        while k != ((2*i)-1):
            if count <= rows-1:
                print("%02d" %(k+1), end=" ")
                count += 1
            else:
                count1 += 1
                print("%02d" %(k+1-(2*count1)), end=" ")
            k += 1
        count1 = count = k = 0
        print()
main()
