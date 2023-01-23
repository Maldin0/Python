'''_'''
def main(temp):
    '''Fever'''
    print('Very High Fever' if temp >= 40 else 'High Fever' if temp >= 39 else
          'Mild Fever' if temp >= 38 else 'No Fever' if temp >= 36 else '')
main(float(input()))
