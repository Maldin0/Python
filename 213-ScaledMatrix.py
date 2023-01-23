'''PSCP Program'''
def main(row, col):
    '''8390-ScaledMatrix 30/10/2022'''
    mat, norm, count = [float(input()) for _ in range(row*col)], [], 0
    mat_stats = max(mat), min(mat)
    for i in mat:
        norm.append((i-mat_stats[1])/(mat_stats[0]-mat_stats[1]))
    for _ in range(row):
        for _ in range(col):
            print('%.2f' % norm[count], end=' ')
            count += 1
        print()
main(int(input()), int(input()))
