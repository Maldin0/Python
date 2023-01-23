'''Sequence XXX'''
def seq(size, feq):
    '''Sequence XXX'''
    for i in range(size):
        disline = ''
        for j in range(size):
            if i == 0 or i == size-1 or i == j or j == 0 or j == size-1 or abs(i+j) == size-1:
                disline += "*"
            else:
                disline += " "
        print(((disline+' ')*feq).rstrip())
seq(int(input()), int(input()))
# 01234
#0*****
#1** **
#2* * *
#3** **
#4*****
