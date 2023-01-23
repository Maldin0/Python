"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def main():
    """PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
    text = input().capitalize()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    if num1 > num2:
        num1, num2 = num2, num1
    if num1 > num3:
        num1, num3 = num3, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if text == "Ascend":
        result = "%.02f, %.02f, %.02f" %(num1, num2, num3)
    elif text == "Descend":
        result = "%.02f, %.02f, %.02f" %(num3, num2, num1)
    print(result)
main()
