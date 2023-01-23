'''PSCP Program'''
def main():
    '''8389-MatrixMN 28/10/2022'''
    matrix = []
    size_n, size_m = int(input()), int(input())
    for _ in range(size_n):
        temp = []
        for _ in range(size_m):
            temp.append(int(input()))
        matrix.append(temp)
    for i in matrix:
        print(*i)


main()
