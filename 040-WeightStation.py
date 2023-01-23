"""WeightStation"""
def isbal(wei, avg, result):
    """Is it balance"""
    if abs(wei-avg) > avg/2:
        result = "Unbalance"
    return result
def weigh():
    """Hell"""
    result = None
    avg = float(input())
    wei1 = float(input())
    wei2 = float(input())
    wei3 = float(input())
    wei4 = avg*4-(wei1+wei2+wei3)
    sumwei = wei1+wei2+wei3+wei4
    result = isbal(wei1, avg, result)
    if result == None:
        result = isbal(wei2, avg, result)
        if result == None:
            result = isbal(wei3, avg, result)
            if result == None:
                result = isbal(wei4, avg, result)
    if sumwei > 15000 or (result == "Unbalance" and sumwei > 15000):
        result = "Overweight"
    if result == None:
        result = "Pass %.02f" %(wei4)
    print(result)
weigh()
