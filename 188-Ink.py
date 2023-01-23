'''PSCP Program'''
def main(data):
    '''8354-Ink 22/10/2022
    By the time I submit this, The Earth has probably already been covered in ink.'''
    for _ in range(data[1]):
        point = [int(i) for i in input().split()]
        print(int(-((3.1416*(point[0]**2+point[1]**2))//-data[0])))
main([int(i) for i in input().split()])
