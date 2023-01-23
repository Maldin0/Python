"""_"""
def func1(num):
    """_"""
    num = num*2
    return num
def func2(num):
    """"""
    num = num/2 + 1
    return num
def main():
    num = float(input())
    print("%.2f" %(func1(func2(float(num)))))
    print("%.2f" %(func2(func1(float(num)))))
main()
