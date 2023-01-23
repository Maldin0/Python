'''PSCP Program'''
def main(roman_num, look_up, total):
    '''8347-Roman (Improved) 21/10/2022'''
    for i, j in enumerate(roman_num):
        total += look_up[j] - (2 * look_up[roman_num[i-1]]) \
                 if i > 0 and look_up[j] > look_up[roman_num[i-1]] else look_up[j]
    print(total)

main(input(), {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}, 0)
