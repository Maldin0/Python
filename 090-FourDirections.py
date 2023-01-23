'''Hello'''
def arrows(direction):
    '''HI'''
    line1, line2, line3, line4, line5 = '', '', '', '', ''
    for i in direction:
        if i == 'U':
            line1 += '  *   '
            line2 += ' ***  '
            line3 += '* * * '
            line4 += '  *   '
            line5 += '  *   '
        elif i == 'D':
            line1 += '  *   '
            line2 += '  *   '
            line3 += '* * * '
            line4 += ' ***  '
            line5 += '  *   '
        elif i == 'L':
            line1 += '  *   '
            line2 += ' *    '
            line3 += '***** '
            line4 += ' *    '
            line5 += '  *   '
        elif i == 'R':
            line1 += '  *   '
            line2 += '   *  '
            line3 += '***** '
            line4 += '   *  '
            line5 += '  *   '
    print(line1.rstrip(), line2.rstrip(), line3.rstrip(), line4.rstrip(), line5.rstrip(), sep='\n')
arrows(input())
