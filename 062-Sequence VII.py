"""Sequence VII"""
def main():
    """Sequence VII"""
    num = int(input())
    for i in range(1, num+1):
        for j in range(i):
            print(j+1, end=" ")
        print()
    for i in range(num-1, 0, -1):
        for j in range(i):
            print(j+1, end=" ")
        print()
main()
