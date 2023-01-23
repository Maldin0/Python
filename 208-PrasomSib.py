'''PSCP Program'''
def main(number, count, total):
    '''8384-PrasomSib 29/10/2022'''
    for j in range(len(number) - 1):
        for i in number[j:]:
            total += int(i)
            if total == 10:
                count, total = count + 1, 0
                break
            if total > 10:
                total = 0
                break
    print(count)
main(input(), 0, 0)
