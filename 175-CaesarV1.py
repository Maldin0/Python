'''PSCP Program'''
def main(shift, code):
    '''8341-CaesarV1 21/10/2022'''
    for char in code:
        temp = ord(char)
        if 65 <= temp <= 90:
            temp += (26 if temp + shift < 65 else -26 if temp + shift > 90 else 0) + shift
        elif 97 <= temp <= 122:
            temp += (26 if temp + shift < 97 else -26 if temp + shift > 122 else 0) + shift
        print(chr(temp), end='')
main(int(input()) % 26, input())
