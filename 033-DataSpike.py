"""Hi"""
def big(num1, num2):
    """because you don't allow us to use 'แม็กซ์'"""
    if num1 > num2:
        num2 = num1
    return num2
def main():
    """And 'ลิส' too"""
    biggest = 0
    last = big(int(input()), biggest)
    last = big(int(input()), last)
    last = big(int(input()), last)
    last = big(int(input()), last)
    last = big(int(input()), last)
    last = big(int(input()), last)
    last = big(int(input()), last)
    last = big(int(input()), last)
    print(last)
main()
