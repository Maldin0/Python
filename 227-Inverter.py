'''_'''
def main(txt, output):
    '''Inverter'''
    for i in txt:
        output += '1' if i == '0' else '0' if i == '1' else ''
    print(int(output) if int(output) else '')
main(input(), '')
