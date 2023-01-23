"""Sequence V"""
def main(num):
    """main"""
    k = 0
    for j in range(num, 0, -1):
        k += 1
        if k%7 == 0:
            print(j)
        else:
            print(j, end=" ")
main(int(input()))
