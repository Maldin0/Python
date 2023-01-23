'''Largest'''
def big(num1, num2, num3):
    """find biggest number"""
    if num1 > num2:
        num1, num2 = num2, num1
    if num1 > num3:
        num1, num3 = num3, num1
    if num2 > num3:
        num2, num3 = num3, num2
    return num3
def main():
    '''Is it truly largest?'''
    num1 = input()
    num2 = input()
    num3 = input()
    nnum1 = int(num1+num2+num3)
    nnum2 = int(num1+num3+num2)
    nnum3 = int(num2+num1+num3)
    nnum4 = int(num2+num3+num1)
    nnum5 = int(num3+num2+num1)
    nnum6 = int(num3+num1+num2)
    total1 = big(nnum1, nnum2, nnum3)
    total2 = big(nnum4, nnum5, nnum6)
    if total1 < total2:
        total = total2
    else:
        total = total1
    print(total)
main()
