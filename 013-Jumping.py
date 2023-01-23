"""Hello"""
def main():
    '''Hi'''
    jumping()
def jumping():
    '''what's up'''
    for i in range(4):
        output_jumping(i+1)
def output_jumping(num):
    '''Yo!!!'''
    for _ in range(3):
        print("Output%d" %(num))
main()
