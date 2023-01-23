'''Bigframe'''


def bframe():
    '''HUhu'''
    line1 = input().rstrip()
    line2 = input().rstrip()
    line3 = input().rstrip()
    line4 = input().rstrip()
    line5 = input().rstrip()
    if len(line1) > len(line2):
        longl = line1
    else:
        longl = line2
    if len(line3) > len(longl):
        longl = line3
    if len(line4) > len(longl):
        longl = line4
    if len(line5) > len(longl):
        longl = line5
    print('*'*(len(longl)+4))
    print('* ', line1, ' '*(len(longl)-(len(line1))), ' *', sep='')
    print('* ', line2, ' '*(len(longl)-(len(line2))), ' *', sep='')
    print('* ', line3, ' '*(len(longl)-(len(line3))), ' *', sep='')
    print('* ', line4, ' '*(len(longl)-(len(line4))), ' *', sep='')
    print('* ', line5, ' '*(len(longl)-(len(line5))), ' *', sep='')
    print('*'*(len(longl)+4))


bframe()
# ***************
# * Hello World *
# * in          *
# * a           *
# * big         *
# * frame       *
# ***************
