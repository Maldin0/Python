"""I'm tried Dad"""
from math import ceil, floor
def main():
    """Hi Tried, I'm Dad"""
    width = int(input())
    height = int(input())
    space = floor(height/2)
    for i in range(height):
        if ceil(height/2) > i >= 0:
            print(" "*space+"*"*width)
            space -= 1
        elif i >= ceil(height/2):
            space += 1
            print(" "*(space+1)+"*"*width)
main()
