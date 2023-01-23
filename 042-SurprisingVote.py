"""SurprisingVote"""
def vote():
    """Hello"""
    sumall = float(input())
    hightest = float(input())
    remain = sumall-hightest
    if remain > hightest:
        remain -= hightest
        if hightest-remain <= 2:
            result = "Not surprising"
        else:
            result = "Surprising"
    elif hightest <= 2:
        result = "Not surprising"
    else:
        result = "Surprising"
    print(result)
vote()
