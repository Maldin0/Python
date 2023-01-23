'''PSCP Program'''
def main():
    '''RemoveTag'''
    txt = input()+' '
    removing = False
    out = []
    buffer = ''
    for char in txt:
        if char == '<':
            removing = True
        if not removing:
            buffer += char
            if char == ' ' and len(buffer.strip()) > 0:
                out.append(buffer.strip())
                buffer = ''
            elif len(buffer.strip()) == 0:
                buffer = ''
        elif removing and len(buffer.strip()) > 0:
            out.append(buffer.strip())
            buffer = ''
        if char == '>':
            removing = False

    print(out)
main()
