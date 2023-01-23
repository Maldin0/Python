'''PSCP Program'''
def main(times, count):
    '''8360-Perfect 23/10/2022'''
    for i in range(6, times, 2):
        count += i if perfect_num(i) else 0
    print(count)
def perfect_num(num):
    '''Check if num is perfect'''
    return num == (num > 1) + sum(i+num//i for i in range(2, int(num**0.5)+1) if num%i == 0)

main(int(input()), 0)
