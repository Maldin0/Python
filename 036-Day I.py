'''Day I'''
def is29():
    '''Check that years is 365 or not'''
    year = int(input())
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)
is29()
