'''PSCP Program'''
import re
def main(word, wrd_lst):
    '''8348-AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain 21/10/2022'''
    for wrd in word:
        count = 0
        for j in list(wrd):
            count += 1 if j in 'aeiou' else 0
        if count >= 2:
            wrd_lst.append(re.sub(r'\W+', '', wrd))
    if len(wrd_lst):
        print(*sorted(wrd_lst), sep="\n")
    else:
        print('Nope')
main(input().lower().split(), [])
