'''PSCP Program'''
def main(times):
    '''8294-Kabata 15/10/2022'''
    for _ in range(times):
        print('no' if input().replace('baka', 'foo').replace('bakka', '')
              .replace('ka', '').replace('ba', '').replace('ta', '') else 'yes')

main(int(input()))
