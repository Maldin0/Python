'''PSCP Program'''
def main(data_dict, output):
    '''8355-SMS 22/10/2022'''
    for _ in range(int(input())):
        button = int(input())
        if button == 1:
            for _ in range(int(input())):
                output = output[:-1] if len(output) else output
        else:
            output += data_dict[button][(int(input()) - 1) % len(data_dict[button])]
    print(output if len(output) else 'null')
main({2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ'}, '')
