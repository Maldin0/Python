'''PSCP Program'''
def main():
    '''8377-GCD_N 29/10/2022'''
    numbers = []
    for i in range(int(input())):
        numbers.append(int(input()))
    if len(numbers) == 1:
        return numbers[0]
    temp = gcd(*numbers[:2])
    for i in numbers[2:]:
        temp = gcd(temp, i)

    return temp

def gcd(num_1, num_2):
    '''GCD v2'''
    for _ in range(num_2):
        if not num_2:
            break
        num_1, num_2 = num_2, num_1 % num_2
    return num_1

print(main())
