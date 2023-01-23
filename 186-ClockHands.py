'''PSCP Program'''
def main(hours, minutes):
    '''8352-ClockHands 23/10/2022'''
    print((hours + minutes/12) >= minutes and ((hours + minutes/12) - minutes) < 6)

main(int(input())*30, int(input())*6)
