'''Yo mama'''
def align(width, position, text):
    '''Do u know candice'''
    if position == "center":
        if (width-len(text))%2 == 1:
            text = " "+text
        out = text.center(width)
    elif position == "left":
        out = text.ljust(width)
    elif position == "right":
        out = text.rjust(width)
    print(out)
align(int(input()), input().lower(), input())
#       banana
#       Caution

