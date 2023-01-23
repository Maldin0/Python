'''PSCP Program'''
def main():
    '''8410-OTP 04/11/2022'''
    while True:
        text = input()
        if text == '0':
            break
        stats = {}
        for i in text:
            stats[i] = 0
        for i in text:
            stats[i] += 1
        val = list(stats.values())
        if len(text) == 4 and val.count(2) == 1 and val.count(1) == 2:
            print('Valid')
        elif len(text) == 6 and ((val.count(2) == 2 and val.count(1) == 2) or val.count(3) == 1):
            print('Valid')
        elif len(text) == 8 and ((val.count(2) == 3 and val.count(1) == 2) or val.count(3) == 2):
            print('Valid')
        else:
            print('Invalid')

main()
