'''PSCP Program'''
def main(text, sta, odr, data):
    '''8379-Gram_v1 29/10/2022'''
    for i, _ in enumerate(text):
        if i == 0:
            continue
        if text[i-1:i+1] not in sta:
            sta[text[i-1:i+1]], odr[text[i-1:i+1]] = 0, i
        sta[text[i-1:i+1]] += 1
    data = sorted([{'O': odr[i], 'W': i, 'C': j} for i, j in sta.items()],
                  key=lambda x: (-x['C'], x['O']))
    print(data[0]['W'], data[0]['C'], sep='\n')

main(input(), {}, {}, [])
