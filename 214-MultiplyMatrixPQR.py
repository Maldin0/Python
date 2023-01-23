'''PSCP Program'''
def main(var_p, var_q, var_r):
    '''8391-MultiplyMatrixPQR 29/10/2022'''
    mat_a = [[int(input()) for _ in range(var_q)] for _ in range(var_p)]
    mat_b = [[int(input()) for _ in range(var_r)] for _ in range(var_q)]
    mat_o = [[0 for _ in range(len(mat_b[0]))] for _ in range(len(mat_a))]
    for val_p in range(var_p):
        for val_r in range(var_r):
            for val_q in range(var_q):
                mat_o[val_p][val_r] += mat_a[val_p][val_q] * mat_b[val_q][val_r]
    for i in mat_o:
        print(*i)
main(int(input()), int(input()), int(input()))
