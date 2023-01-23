'''_'''
def main():
    '''temperature'''
    temp = float(input())
    conversion = input(), input()
    convert_to_cel(conversion[0], conversion[1], temp)

def convert_to_cel(from_unit, to_unit, temp):
    '''Convert to Celsius'''
    if from_unit == 'C':
        convert_to_unit(to_unit, temp)
    elif from_unit == 'F':
        convert_to_unit(to_unit, (temp-32)*(5/9))
    elif from_unit == 'K':
        convert_to_unit(to_unit, temp-273.15)
    elif from_unit == 'R':
        convert_to_unit(to_unit, (temp-491.67)*(5/9))

def convert_to_unit(to_unit, temp):
    '''Convert Celsius to final unit'''
    if to_unit == 'F':
        print("%.2f" % (temp*(9/5)+32))
    elif to_unit == 'K':
        print("%.2f" % (temp+273.15))
    elif to_unit == 'R':
        print("%.2f" % ((temp+273.15)*(9/5)))
    else:
        print("%.2f" % temp)
main()
