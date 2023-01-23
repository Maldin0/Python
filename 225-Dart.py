'''_'''
def main(times, total_score):
    '''Dart'''
    for _ in range(times):
        temp = [float(i) for i in input().split()]
        test = ((temp[0])**2+(temp[1])**2)**0.5
        if test <= 2:
            total_score += 5
        elif test <= 4:
            total_score += 4
        elif test <= 6:
            total_score += 3
        elif test <= 8:
            total_score += 2
        elif test <= 10:
            total_score += 1
    print(total_score)
main(int(input()), 0)
