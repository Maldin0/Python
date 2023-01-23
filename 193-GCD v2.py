'''PSCP Program'''
def main(num_1, num_2):
    '''8359-GCD v2 22/10/2022'''
    for _ in range(num_2):
        if not num_2:
            break
        num_1, num_2 = num_2, num_1 % num_2
    print(num_1)

main(int(input()), int(input()))
