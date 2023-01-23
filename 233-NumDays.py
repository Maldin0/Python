'''_'''
def main():
    '''NumDays'''
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
              7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    start, end = (int(input()), int(input())), (int(input()), int(input()))
    if start[0] > months[start[1]] or end[0] > months[end[1]]:
        print('Impossible')
        return
    start_date, end_date = 0, 0
    for i in range(1, start[1]):
        start_date += months[i]

    for i in range(1, end[1]):
        end_date += months[i]

    print(abs((start_date + start[0]) - (end_date + end[0])))
main()
