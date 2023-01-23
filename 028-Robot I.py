'''hello'''
def  main():
    '''hi'''
    name = input()
    age = float(input())
    if age < 18:
        result = "you can pass."
    else:
        result = "you shall not pass."
    print("%s, %s" %(name, result))
main()
