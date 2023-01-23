'''Haha'''


def main():
    '''MAC'''
    txt, valid = str(input()).upper(), None
    temp = txt.replace("-", "").replace(":", "").replace(".", "")
    #เช็คความถูกต้อง (A-F, 0-9, upper)
    hexa = ('ABCDEF0123456789')
    for i, j in enumerate(temp):
        #เช็คว่า MAC Address มีครบ 12 ตัวไหม
        if i == 11 and valid is not False:
            valid = True
        #เช็คว่า MAC Address ถูกหลัก (A-F, 0-9) ไหม
        if j not in hexa:
            valid = False

    if valid:
        if len(txt) == 17 and (txt[2::3]) == "-----":
            print("VALID 1")

        elif len(txt) == 17 and (txt[2::3]) == ":::::":
            print("VALID 2")

        elif len(txt) == 14 and (txt[4::5]) == "..":
            print("VALID 3")
        else:
            print("ERROR")
    else:
        print('ERROR')


main()
