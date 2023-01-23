"""aa"""
def func1(num):
    """aaa"""
    num = num*2
    return num
def func2(num):
    """aaaa"""
    num = 3*num**4-num**3+2*num**2+10
    return num
def func3(num1, num2, num3):
    """aaaaa"""
    num = (num3+num1)**2-num1*num2+num2**2
    return num
def func4(num1, num2, num3, num4):
    """aaaaaah"""
    num = (num1**2+num2**2-num3**2)/(num4**2-2*num1*num4+2*num1)
    return num
def main():
    """aaaaaaaaah"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    print(func1(func1(num1)))
    print(func2(func1(num1-num2)))
    print(func3(func1(num1+num2), func1(num1+num3), func2(func1(num4**2))))
    print(func4(func3(func1(num1+num2), func1(num1-num3),\
func2(func1(num4**2))), func2(func1(num1-num2)),\
func1(func1(func1(func1(func1(num3))))), num4**8))
main()
