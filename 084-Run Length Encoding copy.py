"""Run Length Encoding"""
def main():
    """Run Length Encoding"""
    word = input()+" "
    nword = word[0]
    count = 0
    first = True
    for i in word:
        if first:
            first = False
        else:
            if i == nword:
                count += 1
                nword = i
            elif i != nword:
                count += 1
                print("%d%s" % (count, nword), end="")
                nword, count = i, 0
main()
