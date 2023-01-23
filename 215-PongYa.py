'''PSCP Program'''
def main(nums):
    '''8392-PongYa 28/10/2022'''
    print('PONG' if int(nums) % 3 == 0 or nums[-1] == '3' else nums)

main(input())
