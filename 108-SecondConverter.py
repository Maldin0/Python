'''SecondConverter'''


def con(now, sec, minn, hour):
    '''U r going to brazil'''
    daysec = sec*minn*hour
    hoursec = sec*minn
    minsec = sec
    hours = now % daysec//hoursec
    mins = (now % daysec) % hoursec//minsec
    secs = ((now % daysec) % hoursec) % minsec
    print("%d:%d:%d" % (hours, mins, secs))


con(int(input()), int(input()), int(input()), int(input()))
