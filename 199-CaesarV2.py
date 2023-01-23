'''PSCP Program'''
def main(code):
    '''8365-CaesarV2 24/10/2022'''
    common_words = ('when', 'which', 'what', 'their', 'this', 'then', 'them', 'these', 'the')
    for shift in range(0, 26):
        out = ''
        for char in code:
            temp = ord(char)
            if 65 <= temp <= 90:
                temp += (26 if temp + shift < 65 else -26 if temp + shift > 90 else 0) + shift
            elif 97 <= temp <= 122:
                temp += (26 if temp + shift < 97 else -26 if temp + shift > 122 else 0) + shift
            out += chr(temp)
        for i in common_words:
            if i in out.lower():
                print(out)
                return
main(input())
