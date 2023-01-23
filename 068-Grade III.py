'''Grade III'''
def grade(num):
    '''I my life is hard cause prof doeen't let me use lis'''
    avg = 0
    for _ in range(num):
        point = float(input())
        if 95 <= point <= 100: #A
            avg += 4.00
        elif 90 <= point < 95: #B+
            avg += 3.50
        elif 85 <= point < 90: #B
            avg += 3.00
        elif 80 <= point < 85: #C+
            avg += 2.50
        elif 75 <= point < 80: #C
            avg += 2.00
        elif 70 <= point < 75: #D+
            avg += 1.50
        elif 65 <= point < 70: #D
            avg += 1.00
        elif 60 <= point < 65: #F+
            avg += 0.50
        elif 0 <= point < 60: #F
            avg += 0.00
    count, out = 0, ''
    gpa = "%.03f" % float(avg/num) # <--- อันนี้คือเกรดเฉลย
    for i in gpa:
        out += i
        count += 1
        if count > 3:
            break
    print(out)
grade(int(input()))
