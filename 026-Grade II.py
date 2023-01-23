'''hello'''
def  main():
    '''hi'''
    grade = float(input())
    if 95 <= grade <= 100:
        result = "A"
    elif 90 <= grade < 95:
        result = "B+"
    elif 85 <= grade < 90:
        result = "B"
    elif 80 <= grade < 85:
        result = "C+"
    elif 75 <= grade < 80:
        result = "C"
    elif 70 <= grade < 75:
        result = "D+"
    elif 65 <= grade < 70:
        result = "D"
    elif 60 <= grade < 65:
        result = "F+"
    elif 0 <= grade < 60:
        result = "F"
    else:
        result = "ERR"
    print(result)
main()
