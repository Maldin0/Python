"""Base 2 number"""
def convert(base_10):
    """from 10 to 2"""
    result = ''
    while base_10 >= 2:
        result += str(base_10 % 2)
        base_10 //= 2
    result += str(base_10)
    result = result[::-1]
    print(result)
convert(int(input()))
