'''hello'''
def  main():
    '''hi'''
    varx = int(input())
    vary = int(input())
    if varx == 0 and vary == 0:
        result = "O"
    elif varx == 0 and vary != 0:
        result = "Y"
    elif vary == 0 and varx != 0:
        result = "X"
    elif varx > 0 and vary > 0:
        result = "Q1"
    elif varx < 0 and vary > 0:
        result = "Q2"
    elif varx < 0 and vary < 0:
        result = "Q3"
    elif varx > 0 and vary < 0:
        result = "Q4"
    print(result)
main()

