'''if u keep staring at that stupid phone u r gonna be stupid'''


def phnum(num, typep):
    '''That's why they're called it smartphone, ma'''
    if typep == 'International':
        res = '+66'
    else:
        res = '0'
    if len(num) == 9:
        res += ' '+num[1:5]+" "+num[5:]
    elif len(num) == 10:
        res += num[1:2]+' '+num[2:6]+' '+num[6:]
    print(res)


phnum(input(), input())
