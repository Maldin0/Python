'''PSCP Program'''
def main(date, month):
    '''8350-Day2011 21/10/2022'''
    print(("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")\
          [((5 if month in (1, 10) else 1 if month in (2, 3, 11) else 4 if month in (4, 7) else\
          6 if month == 5 else 2 if month == 6 else 3 if month in [9, 12] else 0) + date) % 7])
main(int(input()), int(input()))
