'''Sequence XI'''
def seq(num):
    '''Sequence XI'''
    for i in range(-num+1, num):
        for j in range(-num+1, num):
            print("%02d" %(num-max(abs(i), abs(j))), end=" ")
        print()
seq(int(input()))
# แถวที่ i หลักที่ j
# ij  -2 -1 00 01 02
#    _______________
# -2 |01 01 01 01 01
# -1 |01 02 02 02 01
# 00 |01 02 03 02 01
# 01 |01 02 02 02 01
# 02 |01 01 01 01 01
