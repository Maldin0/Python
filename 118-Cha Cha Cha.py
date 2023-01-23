'''3Cha'''


def main():
    '''Cha Cha Cha'''
    wages, work_hours = 0, 0
    for _ in range(int(input())):
        hours = float(input())
        if hours % 1 > 0:
            hours += 1 - (hours % 1)
        if hours > 24:
            hours = 24
        work_hours += hours
    wages += 8720 * work_hours
    print(int(wages))


main()
