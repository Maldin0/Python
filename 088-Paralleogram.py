''''Paralleogram'''
def main(text):
    '''main'''
    for i in range(len(text)*2-1):
        if i <= len(text)-1:
            pos = 0
            newtext = ""
            for j in range(len(text)):
                if i+j >= len(text)-1:
                    newtext += text[pos]
                    pos += 1
            print(newtext.rjust(len(text)))
        elif i > len(text)-1:
            print(text[i-len(text)+1:])
main(input())
#  0123456789
# 0         S
# 1        Sa
# 2       Sam
# 3      Samp
# 4     Sampl
# 5    Sample
# 6   SampleT
# 7  SampleTe
# 8 SampleTex
# 9SampleText
#10ampleText
#11mpleText
#12pleText
#13leText
#14eText
#15Text
#16ext
#17xt
#18t
