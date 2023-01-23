'''ProgressiveTax'''


def taxes(income):
    '''T a X'''
    temp = income
    tax = 0
    if income > 4000000:
        tax += int((temp-4000000)*(35/100))
        temp -= temp-4000000
    if income > 2000000:
        tax += int((temp-2000000)*(30/100))
        temp -= temp-2000000
    if income > 1000000:
        tax += int((temp-1000000)*(25/100))
        temp -= temp-1000000
    if income > 750000:
        tax += int((temp-750000)*(20/100))
        temp -= temp-750000
    if income > 500000:
        tax += int((temp-500000)*(15/100))
        temp -= temp-500000
    if income > 300000:
        tax += int((temp-300000)*(10/100))
        temp -= temp-300000
    if income > 150000:
        tax += int((temp-150000)*(5/100))
        temp -= temp-150000
    print(tax)


taxes(int(input()))
