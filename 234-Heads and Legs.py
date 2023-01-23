'''PSCP Program'''
def main(head, legs):
    '''8422-Heads and Legs 04/11/2022'''
    if legs % 2 != 0 or (head * 2) > legs or legs > (head * 4):
        print('Impossible')
        return
    output = ((2*head)-legs)/(-0.5)
    print(int(output/4), int((legs-output)/2))

main(int(input()), int(input()))
