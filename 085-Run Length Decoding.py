'''Return to monke'''
def decod(text):
    '''Ooga Oogaa'''
    times = ''
    for i in text:
        if i.isnumeric() == True:
            times += i
        elif i.isalpha() == True:
            print(i*int(times), end="")
            times = ''
decod(input())
