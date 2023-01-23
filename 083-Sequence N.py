'''N deez nut'''
def main(num):
    '''HA HA gotem'''
    for i in range(num):
        for j in range(num):
            if (j == 0 or j == num-1) or (i == j):
                print("*", end="")
            else:
                print(" ", end="")
        print()
main(int(input()))
# 012345
#0*    *
#1**   *
#2* *  *
#3*  * *
#4*   **
#5*    *
